import os
import unittest

from flask_script import Manager
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

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(threaded=True, host=os.getenv('BIND_HOST', '127.0.0.1'), port=int(os.getenv('BIND_PORT', '5000')))

@manager.command
def seed():
    if app.environment == 'production':
        print('Run seed on production environment is forbidden. Exit')
        return False
    from app.seed import seed_db; seed_db(app)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
