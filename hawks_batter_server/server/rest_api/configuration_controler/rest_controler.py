""" REST controller for configuration ressource """
import logging
from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.configuration_manager import configuration_service
from .rest_model import ConigurationSchema
from server.common import HawksProbatterException, ErrorCode


logger = logging.getLogger(__name__)

bp = Blueprint("configuration", __name__, url_prefix="/configuration")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class ConfigurationApi(MethodView):
    """API to retrieve or set configuration"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200, schema=ConigurationSchema)
    def get(self):
        """Get current configuration"""

        logger.info(f"GET configuration/")

        # Call configuration service to get current config
        config = configuration_service.get_current_configuration()
        return config


    @bp.doc(responses={400: "BAD_REQUEST"})
    @bp.arguments(ConigurationSchema, location="query")
    @bp.response(status_code=200, schema=ConigurationSchema)
    def post(self, args: ConigurationSchema):
        """Set configuration"""

        logger.info(f"POST configuration/")
        logger.info(f"New config {args}")

        config = configuration_service.set_configuration(pitches=args["pitches"],video=args["video"])
        a = 4 
        return config
        


