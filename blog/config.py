import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABSE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful"
    DEBUG = True
    
