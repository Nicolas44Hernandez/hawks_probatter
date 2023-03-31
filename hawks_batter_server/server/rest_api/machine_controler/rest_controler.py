""" REST controller for machine manager ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.video_manager import video_manager_service
from .rest_model import MachineStatusSchema
from server.common import HawksProbatterException, ErrorCode


logger = logging.getLogger(__name__)

bp = Blueprint("running", __name__, url_prefix="/running")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class MachineManagementApi(MethodView):
    """API to manage machine status"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200, schema=MachineStatusSchema)
    def get(self):
        """Get current machine status"""

        logger.info(f"GET running/")

        # Call video manager service to get current status
        return video_manager_service.get_current_machine_status()


    @bp.doc(responses={400: "BAD_REQUEST"})
    @bp.arguments(MachineStatusSchema, location="query")
    @bp.response(status_code=200, schema=MachineStatusSchema)
    def post(self, args: MachineStatusSchema):
        """Set machine status"""

        logger.info(f"POST running/")
        logger.info(f"New status {args}")

        if args["running"]:
            video_manager_service.new_game()
        else:
            video_manager_service.exit_game()
        return video_manager_service.get_current_machine_status()
        


