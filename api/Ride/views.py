'''rides views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.user import User

ride_blueprint = Blueprint('ride', __name__)


class Ride(MethodView):
    ''' a view class with methods to hande ride(s)'''
    def post(self):
        ''' class method which allows user to sign up'''
    
    def delete(self):
        '''canacel ride'''

class GetRides(MethodView):
    ''' a view class for rides'''
    def get(self):
        ''' class method which fetch all rides'''

class GetRide(MethodView):
    ''' a view class for a single ride'''
    def get(self):
        ''' class method which allow user retrieve a siingle ride'''



ride_blueprint.add_url_rule(
    '/rides', view_func=Ride.as_view('rides'), methods=['POST'])
ride_blueprint.add_url_rule(
    '/rides', view_func=GetRides.as_view('getrides'), methods=['GET'])
ride_blueprint.add_url_rule(
    '/rides/<rideid>', view_func=GetRide.as_view('getride'), methods=['GET'])
