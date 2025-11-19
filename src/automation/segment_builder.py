thonfrom .utils.logger import get_logger

logger = get_logger(__name__)

class SegmentBuilder:
 def __init__(self, config):
 self.config = config

 def build_segments(self, payload):
 segments = {}
 for name, rule in self.config.get("rules", {}).items():
 field, expected = rule.get("field"), rule.get("equals")
 segments[name] = payload.get(field) == expected
 logger.info(f"Segments built: {segments}")
 return {"payload": payload, "segments": segments}