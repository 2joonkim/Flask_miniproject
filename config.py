from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:0000@localhost/oz"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 5
    SQLALCHEMY_POOL_RECYCLE = 1800
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_ECHO = False
    reload = True

    # smorest 설정
    API_TITLE = 'API TEST'  # API 제목
    API_VERSION = '1.0'  # API 버전
    API_DESCRIPTION = 'SURVEY API'  # API 설명

    # OpenAPI 버전 설정
    OPENAPI_VERSION = "3.0.0"
