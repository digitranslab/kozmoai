import logging

from pydantic import BaseModel, field_serializer
from pydantic_core import PydanticSerializationError

from kozmoai.schema.log import LoggableType
from kozmoai.serialization.serialization import serialize

logger = logging.getLogger(__name__)


class Log(BaseModel):
    name: str
    message: LoggableType
    type: str

    @field_serializer("message")
    def serialize_message(self, value):
        try:
            return serialize(value)
        except UnicodeDecodeError:
            return str(value)  # Fallback to string representation
        except PydanticSerializationError:
            return str(value)  # Fallback to string for Pydantic errors
