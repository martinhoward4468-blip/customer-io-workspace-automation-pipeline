thonfrom .utils.logger import get_logger
from .utils.schema_validator import validate_schema

logger = get_logger(__name__)

class EventMapper:
 def __init__(self, config):
 self.config = config

 def map_event(self, event):
 validate_schema(event, self.config.get("event_schema", {}))
 event_type = event.get("type")
 mapping = self.config.get("mappings", {}).get(event_type)

 if not mapping:
 logger.error(f"No mapping defined for event type: {event_type}")
 raise ValueError("Invalid event type")

 mapped = {k: event.get(v) for k, v in mapping.items()}
 logger.info(f"Event mapped: {mapped}")
 return mapped