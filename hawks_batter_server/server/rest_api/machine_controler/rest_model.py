"""REST API models for relays manager package"""

from marshmallow import Schema
from marshmallow.fields import Boolean


class MachineStatusSchema(Schema):
    """REST ressource for machine status"""

    running = Boolean(required=True, allow_none=False)
