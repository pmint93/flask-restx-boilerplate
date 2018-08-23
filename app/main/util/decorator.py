from flask import request
from flask import current_app as app
from functools import wraps
import time

def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.headers.get('Authorization') is None:
            return { 'message': 'Missing Authorization header' }, 401
        auth = request.authorization
        if auth is None:
            return { 'message': 'Invalid Authorization header' }, 401
        kwargs['basic_auth'] = auth
        return f(*args, **kwargs)

    return decorated

def authenticate_user(f=None, **config):
    def real_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # Just nothing ;)
            return f(*args, **kwargs)

        return decorated

    if f is None:
        return real_decorator
    else:
        return real_decorator(f)

def authorize_access(f=None, **config):
    def real_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # Just nothing ;)
            return f(*args, **kwargs)

        return decorated

    if f is None:
        return real_decorator
    else:
        return real_decorator(f)

def slowed_action(f=None, **config):
    # Simply make request to be slow by delayed action execute :)))
    def real_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            delayed_time = config.get('seconds')
            if not delayed_time:
                delayed_time = 2 # Default delayed time
            delayed_time = int(delayed_time)
            time.sleep(delayed_time)
            return f(*args, **kwargs)

        return decorated

    if f is None:
        return real_decorator
    else:
        return real_decorator(f)
