'''
___init__.py
main API config  file
'''

from flask_api import FlaskAPI

# local imports
from api.config import CONFIGS
from .Auth.views import auth_blueprint
from .Ride.views import ride_blueprint


def create_app(config_param):
    ''' function that receives configaration and creates the app'''
    app = FlaskAPI(__name__)
    app.config.from_object(CONFIGS[config_param])
    app.url_map.strict_slashes = False
    app.register_blueprint(auth_blueprint, url_prefix='/auth/api/v1')
    app.register_blueprint(ride_blueprint, url_prefix='/api/v1')
    return app
