import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_super_strong_secret_key_hehe')
    DEBUG = False
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
    # Sentry config
    SENTRY_CONFIG = {
        'dsn': os.getenv('SENTRY_CONFIG_DSN', 'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@sentry.k8s.vn/44?verify_ssl=0')
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SENTRY_CONFIG = None


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)
