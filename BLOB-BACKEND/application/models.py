from .database import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(128), nullable=False)
    user_email = db.Column(db.String(128), unique=True)  # Added uniqueness for emails
    password = db.Column(db.String(128))
    is_privileged = db.Column(db.String(128), default=0)
    profile_pic= db.Column(db.String(128), default=None)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'is_privileged': self.is_privileged,
            'profile_pic': self.profile_pic
        }

    
class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Change to Integer
    admin_name = db.Column(db.String(128))
    admin_email = db.Column(db.String(128), unique=True)  # Ensuring unique emails
    password = db.Column(db.String(128))
    profile_pic= db.Column(db.String(128), default=None)

    def to_dict(self):
        return {
            'admin_id': self.admin_id,
            'admin_name': self.admin_name,
            'admin_email': self.admin_email,
            'profile_pic': self.profile_pic
        }

class Blog(db.Model):
    __tablename__ = 'blog'
    blog_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blog_name = db.Column(db.String(128))
    blog_content = db.Column(db.String(5048))
    blog_subtitle = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='blogs')  # Define relationship with User
    
    def to_dict(self):
        return {
            'blog_id': self.blog_id,
            'blog_name': self.blog_name,
            'blog_content': self.blog_content,
            'blog_subtitle': self.blog_subtitle,
            'user_id': self.user_id
        }


class AdminBlog(db.Model):
    __tablename__ = 'admin_blog'
    admin_blog_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_blog_name = db.Column(db.String(128))
    admin_blog_content = db.Column(db.String(5048))
    admin_blog_subtitle = db.Column(db.String(128))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    admin = db.relationship('Admin', backref='admin_blogs')  # Relationship with Admin
    
    def to_dict(self):
        return {
            'admin_blog_id': self.admin_blog_id,
            'admin_blog_name': self.admin_blog_name,
            'admin_blog_content': self.admin_blog_content,
            'admin_blog_subtitle': self.admin_blog_subtitle,
            'admin_id': self.admin_id
        }
        
        
class User_issue(db.Model):
    __tablename__ = 'user_issue'
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    doi = db.Column(db.DateTime)
    request_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(128))
    re_issue = db.Column(db.Integer, default=1)
    
    user = db.relationship('User', backref='user_issues')  # Relationship with User
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'doi': self.doi,
            'request_date': self.request_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
            'status': self.status,
            're_issue': self.re_issue
        }


     
from datetime import datetime   
class BlogAnalysis(db.Model):
    __tablename__ = 'blog_analysis'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    popularity_rate = db.Column(db.Float, nullable=False)
    total_views = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'post_name': self.post_name,
            'category': self.category,
            'time_posted': self.time_posted.strftime('%Y-%m-%d %H:%M:%S'),
            'popularity_rate': self.popularity_rate,
            'total_views': self.total_views,
        }
    
    def __repr__(self):
        return f'<BlogAnalysis {self.post_name} in category {self.category}>'
    
class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.blog_id'))
    admin_blog_id = db.Column(db.Integer, db.ForeignKey('admin_blog.admin_blog_id'))
    admin_id=db.Column(db.Integer,db.ForeignKey('admin.admin_id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'))
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_name=db.Column(db.String(128),nullable=False)

    def to_dict(self):
        """
        Converts the object into a dictionary representation.
        """
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'admin_id': self.admin_id,
            'admin_blog_id': self.admin_blog_id,
            'user_id': self.user_id,
            'review_name':self.review_name,
            'description': self.description,
            'rating': self.rating
        }

    def __repr__(self):
        """
        Returns a string representation of the object for debugging.
        """
        return f"<Reviews(id={self.id}, blog_id={self.blog_id}, admin_blog_id={self.admin_blog_id}, admin_id={self.admin_id}, user_id={self.user_id}, rating={self.rating})>"


