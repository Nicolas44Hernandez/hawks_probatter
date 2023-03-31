"""REST API models for relays manager package"""

from marshmallow import Schema
from marshmallow.fields import Integer, String


class ConigurationSchema(Schema):
    """REST ressource for configuration"""

    pitches = Integer(required=True, allow_none=False)
    video = String(required=True, allow_none=False)
