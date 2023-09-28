from flask import Flask
from flask_caching import Cache
from raven.contrib.flask import Sentry
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_mongoengine import MongoEngine

from .config import Config as config

cache = Cache()
sentry = Sentry()
db = MongoEngine()


def create_app(env_name):
    app = Flask(__name__)
    # Save environment name to current app context
    app.environment = env_name
    # Configure application from evironment name
    app.config.from_object(config)
    # Init application cache
    cache.init_app(app, config={'CACHE_TYPE': app.config['CACHE_TYPE']})
    # Init sentry for error reporting
    if app.config.get('SENTRY_CONFIG'):
        sentry.init_app(app)
    # Fix Flask when deployed behind proxy
    app.wsgi_app = ProxyFix(app.wsgi_app)
    # Init database connection
    db.init_app(app)

    return app
