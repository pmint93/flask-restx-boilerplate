from flask_restplus import Api, Namespace
from flask import Blueprint
from flask_cors import CORS

from .main.controller.health_controller   import api as health_namespace

blueprint = Blueprint('api', __name__)

# CORS(blueprint, origins=['*'], allow_headers=['*'], expose_headers=['*'])

api = Api(blueprint,
          title='flask-restplus-boilerplate',
          version='1.0',
          description='flask-restplus-boilerplate service'
          )

api.add_namespace(health_namespace, path='/health')
