""" REST controller for configuration ressource """
import logging
from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.configuration_manager import configuration_service
from server.managers.videos_list_manager import videos_list_manager_service
from server.managers.video_manager import video_manager_service
from .rest_model import ConigurationSchema, VideoSchema
from server.common import HawksProbatterException, ErrorCode


logger = logging.getLogger(__name__)

bp = Blueprint("configuration", __name__, url_prefix="/api/configuration")
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

        return configuration_service.set_configuration(pitches=args["pitches"],video=args["video"])
        

@bp.route("/videos_list")
class VideosListApi(MethodView):
    """API to retrieve videos_list"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200, schema=VideoSchema(many=True))
    def get(self):
        """Get videoslist"""

        logger.info(f"GET configuration/videos_list")

        # Call video list manager service to get videos list
        return videos_list_manager_service.get_videos_list()
    

@bp.route("/image_setup")
class ImageSetupApi(MethodView):
    """API to launch/end image setup"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200)
    def get(self):
        """Launch / stop image setup"""

        logger.info(f"GET configuration/image_setup")

        # Call video manager to launch image setup
        return video_manager_service.setup_image()


