'''views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from api.models.user import User

ride_blueprint = Blueprint('ride', __name__)
