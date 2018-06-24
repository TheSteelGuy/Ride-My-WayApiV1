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
 

class SignIn(MethodView):
    ''' a view class for signin'''
    def post(self):
        ''' class method which allows user to sign in'''

class Logout(MethodView):
    ''' a view class for logout '''
    def post(self):
        ''' class method which allows user to sign out'''


auth_blueprint.add_url_rule(
    '/signup', view_func=SignUp.as_view('signup'), methods=['POST'])
auth_blueprint.add_url_rule(
    '/signin', view_func=SignIn.as_view('signin'), methods=['POST'])
auth_blueprint.add_url_rule(
    '/logout', view_func=Logout.as_view('logout'), methods=['POST'])