from flask import Flask
from flask_caching import Cache
from raven.contrib.flask import Sentry

from .config import config_by_name

cache = Cache()
sentry = Sentry()


def create_app(env_name):
    app = Flask(__name__)
    # Save environment name to current app context
    app.environment = env_name
    # Configure application from evironment name
    app.config.from_object(config_by_name[env_name])
    # Init application cache
    cache.init_app(app, config={'CACHE_TYPE': app.config['CACHE_TYPE']})
    # Init sentry for error reporting
    if app.config.get('SENTRY_CONFIG'):
        sentry.init_app(app)

    return app