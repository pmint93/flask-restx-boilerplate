import os
import unittest

from flask_script import Manager

from app import blueprint
from app.main import create_app

app = create_app(os.getenv('APPLICATION_ENV') or 'development')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(threaded=True)

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
