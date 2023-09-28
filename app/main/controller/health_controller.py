from flask import request, Response
from flask import current_app as app
from flask_restx import Resource, Namespace, fields


api = Namespace('health', description='Healthcheck API')


@api.route('')
class HealthcheckAPI(Resource):
    def get(self, **kwargs):
        """healcheck API"""
        return {
            'message': "I'm good, thanks"
        }
