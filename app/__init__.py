from flask_restx import Api, Namespace
from flask import Blueprint

from .main.controller.health_controller   import api as health_namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='flask-restx-boilerplate',
          version='1.0',
          description='flask-restx-boilerplate service'
          )

api.add_namespace(health_namespace, path='/health')
