'''views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.user import User

auth_blueprint = Blueprint('auth', __name__)

users = list()

class SignUp(MethodView):
    ''' a view class for sign up'''
    def post(self):
        ''' class method which allows user to sign up'''
        username = request.json.get('username')
        phone = request.json.get('phone')
        password = request.json.get('password')
        confirm_p = request.json.get('confirm')
        if username and phone and password and confirm_p:
            if not User.check_phone(phone):
                return make_response(jsonify(
                    {'message':'enter phone contact in 072-333-2222 format'}
                )), 409
            if not User.verify_password(password, confirm_p):
                return make_response(jsonify(
                    {'message': 'Ensure password and confirm password matches.'}
                )), 409
            check_pass = User.p_strength(password)
            if not check_pass:
                return make_response(jsonify(
                    {'message': check_pass}
                )), 409
            
            user_obj = User(username, phone, password, confirm_p)
            user = User.serialize_user(user_obj)
            users.append(user)
            return make_response(jsonify(
                {'message': 'welcome to our community,{}'.format(user['username'])}
            )), 201
        return make_response(jsonify(
            {'message': 'ensure you have provide all required details'}
        )), 400

class SignIn(MethodView):
    ''' a view class for signin'''
    def post(self):
        ''' class method which allows user to sign in'''
        username = request.json.get('username')
        password = request.json.get('password')
        if username and password:
            user = filter(lambda dict_:dict_['username']==username, users)
            password = list(filter(lambda dict_:dict_['password']==password, users))
            if user and password:
                return make_response(jsonify(
                    {'message':'you have succefully logged in'}
                )), 200
            return make_response(jsonify(
                {'message':'wrong credentials'}
            )), 401
        return make_response(jsonify(
            {'message':'ensure you have provide all required details'}
        )), 400

class Logout(MethodView):
    ''' a view class for logout '''
    def post(self):
        ''' class method which allows user to sign out'''
        return make_response(jsonify(
            {'message':'succesfully logged out'}
        )), 200


auth_blueprint.add_url_rule(
    '/signup', view_func=SignUp.as_view('signup'), methods=['POST'])
auth_blueprint.add_url_rule(
    '/signin', view_func=SignIn.as_view('signin'), methods=['POST'])
auth_blueprint.add_url_rule(
    '/logout', view_func=Logout.as_view('logout'), methods=['POST'])