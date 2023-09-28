import os
import logging
from flask_cors import CORS
from app import blueprint
from app.main import create_app

app = create_app(os.getenv('APPLICATION_ENV') or 'development')
if app.config.get('ENABLE_CORS', False):
    CORS(
        blueprint,
        origins=app.config.get('CORS_ALLOW_ORIGINS') or ['*'],
        methods=app.config.get('CORS_ALLOW_METHODS') or ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'],
        allow_headers=app.config.get('CORS_ALLOW_HEADERS') or ['*'],
        expose_headers=app.config.get('CORS_EXPOSE_HEADERS') or None,
        supports_credentials=app.config.get('CORS_ALLOW_CREDENTIALS') or False,
        max_age=app.config.get('CORS_MAX_AGE') or None
    )
app.register_blueprint(blueprint)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
