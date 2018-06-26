'''rides views.py'''
from datetime import datetime
# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.ride import Ride

ride_blueprint = Blueprint('ride', __name__)

rides = list()
joins_for_a_ride = list()


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
                        {'message': 'enter date in the format of dd-mm-YYYY'}
                    )), 409

            if date < date.today():
                return make_response(
                    jsonify({
                        'message': 'rides can only be of the present and the future'
                    })), 409
            if Ride.does_ride_exist(rides, dest, time):
                return make_response(jsonify(
                    {'message': 'you are already offering a ride to this destination on this date'})), 409
            id_count = 1
            for item in rides:
                id_count += 1
            ride = Ride(dest, date, time, meet_p, charges)
            ride_dict = Ride.serialize_ride(ride, id_count)
            rides.append(ride_dict)
            return make_response(jsonify({'message': 'succesfully created ride to {} on {}'.format(
                ride_dict['destination'], ride_dict['date'])})), 201

        return make_response(jsonify(
            {'message': 'ensure you have provide all required details'}
        )), 400

    def delete(self, rideid):
        '''cancel ride'''
        ride_by_id = Ride.get_ride(rides, int(rideid))
        if ride_by_id:
            rides.remove(ride_by_id[0])
            return make_response(jsonify(
                {'details of cancelled ride': ride_by_id[0]}
            )), 200
        return make_response(jsonify(
            {'message': 'the ride you are trying to cancel does not exist'}
        )), 404


class GetRides(MethodView):
    ''' a view class for rides'''

    def get(self):
        ''' class method which fetch all rides'''
        if not rides:
            return make_response(jsonify(
                {'message': 'no ride currently avilable'}
            )), 204
        return make_response(jsonify(
            {'Avilable rides': rides}
        )), 200


class GetRide(MethodView):
    ''' a view class for a single ride'''

    def get(self, rideid):
        ''' class method which allow user retrieve a siingle ride'''
        ride_by_id = Ride.get_ride(rides, int(rideid))
        if ride_by_id:
            return make_response(jsonify(
                {'ride': ride_by_id}
            )), 200
        return make_response(jsonify(
            {'message': 'ride you specified does not exist'}
        )), 404


class JoinRide(MethodView):
    ''' class request to join ride'''

    def post(self, rideid):
        '''method which handles join ride'''
        ride_by_id = Ride.get_ride(rides, int(rideid))
        if not ride_by_id:
            return make_response(jsonify(
                {'message': 'the ride tou are looking for nolonger exists.'}
            )), 404
        join_ride = {
            'ride_id': rideid,
            'phone_contact': '072-111-1111',
            'username': 'collo'
        }
        joins_for_a_ride.append(join_ride)
        return make_response(jsonify(
            {'message': 'you have succefully sent a join request, you will receive notification soon'}
        )), 201


ride_blueprint.add_url_rule(
    '/rides/<rideid>/requests',
    view_func=JoinRide.as_view('joinride'),
    methods=['POST'])
ride_blueprint.add_url_rule(
    '/rides', view_func=RideOffer.as_view('rides'), methods=['POST'])
ride_blueprint.add_url_rule(
    '/rides', view_func=GetRides.as_view('getrides'), methods=['GET'])
ride_blueprint.add_url_rule(
    '/rides/<rideid>', view_func=GetRide.as_view('getride'), methods=['GET'])
ride_blueprint.add_url_rule(
    '/rides/<rideid>/cancel',
    view_func=RideOffer.as_view('cancelride'),
    methods=['DELETE'])
