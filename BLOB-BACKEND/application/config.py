import os
cur_directory=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFIATIONS=False
    
    
class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(cur_directory,"../db_directory")
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(SQLITE_DB_DIR,"dmp.sqlite3")
    DEBUG=True
    
   