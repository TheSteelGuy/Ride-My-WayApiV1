'''views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.user import User, BlacklistTokens
from api.authenticator import token_required
from api.tables import CONN

auth_blueprint = Blueprint('auth', __name__)


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
                    {'message': 'enter phone contact in 072-333-2222 format'}
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
            if User.does_user_exist(phone):
                return make_response(jsonify(
                    {'message': 'a user with that phone contact already exist'}
                )), 409
            user = User(username, phone, password,confirm_p)
            user.save_user()
            cursor = CONN.cursor()
            cursor.execute('SELECT id FROM users WHERE phone_contact =%s',(user.phone,))
            row = cursor.fetchone()
            auth_token=user.generate_token(row[0])
            return make_response(jsonify(
                {'message': 'registration successfull','auth_token':auth_token.decode()}
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
            cursor = CONN.cursor()
            cursor.execute('SELECT id FROM users WHERE username =%s AND password =%s',(username,password))
            tuple_ = cursor.fetchone()
            if tuple_:
                return make_response(jsonify(
                    {'message': 'you have succefully logged in','auth_token':User.generate_token(tuple_[0])}
                )), 200
            return make_response(jsonify(
                {'message': 'wrong credentials'}
            )), 401
        return make_response(jsonify(
            {'message': 'ensure you have provide all required details'}
        )), 400


class Logout(MethodView):
    ''' a view class for logout '''

    def post(self):
        ''' class method which allows user to sign out'''
        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split("Bearer ")[1]
        if auth_token and not BlacklistTokens.verify_token(auth_token):
            auth_data = User.decode_token(auth_token)
            if not isinstance(auth_data, str):
                blacklist_token = BlacklistTokens(auth_token)
                try:
                    blacklist_token.save_token(auth_token)
                    return make_response(
                        jsonify({
                            'message': 'you have successfully logged out'
                        })), 200
                except Exception as e:
                    string = 'An exception of type {0} occurred. Arguments:\n{1!r}'
                    message = string.format(type(e).__name__, e.args)
                    return make_response(jsonify({"message": message})), 500
            return make_response(jsonify({"message": auth_data})), 404
        return make_response(
            jsonify({
                'message': 'please provide a valid token'})), 403

auth_blueprint.add_url_rule(
    '/signup', view_func=SignUp.as_view('signup'), methods=['POST'])

auth_blueprint.add_url_rule(
    '/login', view_func=SignIn.as_view('login'), methods=['POST'])

auth_blueprint.add_url_rule(
    '/logout', view_func=Logout.as_view('logout'), methods=['POST'])