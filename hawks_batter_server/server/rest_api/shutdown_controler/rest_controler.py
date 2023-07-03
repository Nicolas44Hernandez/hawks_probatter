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
    """API to manage machine status"""

    @bp.doc(
        responses={400: "BAD_REQUEST", 404: "NOT_FOUND"},
    )
    @bp.response(status_code=200)
    def get(self):
        """Shutdown RPI"""

        logger.info(f"GET shutdown/")
        #return os.system("sudo shutdown -h now")
        command="shutdown -h now"
        return os.popen("sudo -S %s"%(command), 'w').write('pi')
