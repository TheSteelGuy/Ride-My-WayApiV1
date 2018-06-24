'''rides views.py'''
from datetime import datetime
# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.ride import Ride

ride_blueprint = Blueprint('ride', __name__)

rides = list()


class RideOffer(MethodView):
    ''' a view class with methods to hande ride(s)'''
    def post(self):
        ''' class method which allows user to sign up'''
        dest = request.json.get('destination')
        date = request.json.get('date')
        time = request.json.get('time')
        meet_p = request.json.get('meetpoint')
        charges = request.json.get('charges')
        if dest and date and time and meet_p and charges:
            try:
                date = datetime.strptime(date, '%d-%m-%Y').date()
            except ValueError:
                return make_response(
                    jsonify(
                        {'message':'enter date in the format of dd-mm-YYYY'}
                        )), 409

            if date < date.today():
                return make_response(
                    jsonify({
                        'message': 'rides can only be of the present and the future'
                    })), 409
            ride = Ride(dest, date, time, meet_p, charges)
            ride_dict = Ride.serialize_ride(ride)
            rides.append(ride_dict)
            return  make_response(jsonify(
                {'message':'succesfully created ride to {} on {}'.format(ride_dict['destination'],ride_dict['date'])}
            )), 201

        return make_response(jsonify(
            {'message':'ensure you have provide all required details'}
        )), 400
    
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
    '/rides', view_func=RideOffer.as_view('rides'), methods=['POST'])
ride_blueprint.add_url_rule(
    '/rides', view_func=GetRides.as_view('getrides'), methods=['GET'])
ride_blueprint.add_url_rule(
    '/rides/<rideid>', view_func=GetRide.as_view('getride'), methods=['GET'])
