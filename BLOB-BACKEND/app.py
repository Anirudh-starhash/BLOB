import os
from flask import Flask
from application.database import db
from application.config import LocalDevelopmentConfig
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from application.user_controllers import *
from application.blog_controllers import *
from application.admin_controllers import *
from application.review_controllers import *
from application.api import *
from flask_restful import Resource,Api

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module=r'flask_caching')

app=None
celery=None
api=None

def create_app():
    global app,cache
    app = Flask(__name__)
    # Import blueprints here to avoid circular imports
    app.register_blueprint(user_blueprint, url_prefix='/api')
    app.register_blueprint(lib_blueprint, url_prefix='/api')
    app.register_blueprint(blog_blueprint, url_prefix='/api')
    app.register_blueprint(review_blueprint, url_prefix='/api')
    app.register_blueprint(swagger_admin_ui_blueprint, url_prefix='/api/admin/docs')
    app.register_blueprint(swagger_user_ui_blueprint, url_prefix='/api/user/docs')
    app.register_blueprint(swagger_blog_ui_blueprint, url_prefix='/api/blog/docs')
    app.register_blueprint(swagger_review_ui_blueprint, url_prefix='/api/review/docs')
   
   

    if os.getenv('ENV', "development") == "production":
        app.logger.warning("Currently no production config is set up")
        raise Exception("Currently no production config is set up")
    else:
        app.logger.info("Starting local development")
        print('Starting local Development')
        app.config.from_object(LocalDevelopmentConfig)
       
        app.app_context().push()
        
        
       
        
        app.config['CACHE_TYPE'] = 'RedisCache'
        app.config['CACHE_REDIS_HOST'] = 'localhost'
        app.config['CACHE_REDIS_PORT'] = 6379
        app.config['CACHE_REDIS_DB'] = 0
        app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
            
        app.app_context().push()
        
        app.config['SECRET_KEY'] = "Secret is meant to be Secret"
        app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
        print("After setting CACHE_TYPE:", app.config['CACHE_TYPE'])
        
        api=Api(app)
        app.app_context().push()
        
       
        app.app_context().push()
        
        
        db.init_app(app)
        app.app_context().push()
        # Initialize Celery and Mail after app config is updated
        app.logger.info("App Setup Complete")

        return app,api
    
app,api=create_app()
CORS(app)
migrate=Migrate(app)
jwt=JWTManager(app)
cache=Cache(app,config=app.config)
print("Cache type in cache object:", cache.config['CACHE_TYPE'])

@app.route("/")
def home():
    return jsonify({
        'msg':'Hey you are connected to backend!'
    }),200

@app.route("/cache")
@cache.cached(timeout=30)
def index():
    return jsonify({
        'msg':'Cache is Working'
        }),200

@app.errorhandler(404)
def page_not_found(self):
    return jsonify({
        'msg':'Page Not found'
    }),404
    
@app.errorhandler(401)
def not_authorized(self):
    return jsonify({
        'msg':'Not Authorized'
    }),401
    

with app.app_context():
    db.create_all()
    
if __name__=="__main__":
    port = os.getenv("PORT", 5000)  # Render sets this automatically
    app.run(debug=True,host="0.0.0.0",port=int(port))