import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    DATABASE_URI = os.getenv('DATABASE_URL')
    

class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE_URI = 'postgresql://localhost/shop_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI= 'postgresql://localhost/shoptest_db'
    TESTING = True

class ProductiongConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI= ''
    TESTING = True

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}

