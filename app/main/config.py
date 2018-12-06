import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_super_strong_secret_key_hehe')
    DEBUG = False
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
    # Sentry config
    SENTRY_CONFIG = {
        'dsn': os.getenv('SENTRY_CONFIG_DSN', 'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@sentry.k8s.vn/44?verify_ssl=0')
    } if os.getenv('SENTRY_CONFIG', 'False').lower() != 'false' else False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'flask-restplus-boilerplate_development',
        'host': os.getenv('MONGO_HOST', '127.0.0.1'),
        'port': os.getenv('MONGO_PORT', 27017),
    }


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'flask-restplus-boilerplate_test',
        'host': os.getenv('MONGO_HOST', '127.0.0.1'),
        'port': os.getenv('MONGO_PORT', 27017),
    }


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'flask-restplus-boilerplate',
        'host': os.getenv('MONGO_HOST', '127.0.0.1'),
        'port': os.getenv('MONGO_PORT', 27017),
    }


config_by_name = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)
