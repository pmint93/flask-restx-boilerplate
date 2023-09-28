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
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DBNAME', 'flask-restplus-boilerplate'),
        'host': os.getenv('MONGO_HOST', '127.0.0.1'),
        'port': os.getenv('MONGO_PORT', 27017),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASS'),
    }
    # CORS
    ENABLE_CORS             = True if (os.getenv('ENABLE_CORS') or 'False').lower() != 'false' else False
    CORS_ALLOW_ORIGINS      = os.getenv('CORS_ALLOW_ORIGINS',  '').split(',')
    CORS_ALLOW_METHODS      = os.getenv('CORS_ALLOW_METHODS',  '').split(',')
    CORS_ALLOW_HEADERS      = os.getenv('CORS_ALLOW_HEADERS',  '').split(',')
    CORS_EXPOSE_HEADERS     = os.getenv('CORS_EXPOSE_HEADERS', '').split(',')
    CORS_ALLOW_CREDENTIALS  = True if (os.getenv('CORS_ALLOW_CREDENTIALS') or 'False').lower() != 'false' else False
    CORS_MAX_AGE            = int(os.getenv('CORS_MAX_AGE')) if os.getenv('CORS_MAX_AGE') else None
