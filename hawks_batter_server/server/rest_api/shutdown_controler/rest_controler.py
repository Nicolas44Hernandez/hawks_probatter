""" REST controller for machine manager ressource """
import logging
import os
from flask.views import MethodView
from flask_smorest import Blueprint

logger = logging.getLogger(__name__)

bp = Blueprint("shutdown", __name__, url_prefix="/shutdown")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class MachineManagementApi(MethodView):
    """API to shutdown system"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200)
    def get(self):
        """Shutdown RPI"""

        logger.info(f"GET shutdown/")
        command="shutdown -h now"
        return os.popen("sudo -S %s"%(command), 'w').write('pi')

@bp.route("/reboot")
class MachineManagementApi(MethodView):
    """API to reboot system status"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200)
    def get(self):
        """Reboot RPI"""

        logger.info(f"GET shutdown/reboot")
        command="reboot now"
        return os.popen("sudo -S %s"%(command), 'w').write('pi')