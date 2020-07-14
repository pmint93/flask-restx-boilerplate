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
    # CORS
    ENABLE_CORS             = os.getenv('ENABLE_CORS')
    CORS_ALLOW_ORIGINS      = os.getenv('CORS_ALLOW_ORIGINS')
    CORS_ALLOW_METHODS      = os.getenv('CORS_ALLOW_METHODS')
    CORS_ALLOW_HEADERS      = os.getenv('CORS_ALLOW_HEADERS')
    CORS_EXPOSE_HEADERS     = os.getenv('CORS_EXPOSE_HEADERS')
    CORS_ALLOW_CREDENTIALS  = os.getenv('CORS_ALLOW_CREDENTIALS')
    CORS_MAX_AGE            = int(os.getenv('CORS_MAX_AGE')) if os.getenv('CORS_MAX_AGE') else None
