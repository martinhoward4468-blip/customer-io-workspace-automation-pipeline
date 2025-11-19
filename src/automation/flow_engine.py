thonfrom .utils.logger import get_logger

logger = get_logger(__name__)

class FlowEngine:
 def __init__(self, config):
 self.config = config

 def run_flows(self, data):
 active_flows = []
 for flow_name, flow_def in self.config.get("flows", {}).items():
 required_segment = flow_def.get("segment")
 if data["segments"].get(required_segment):
 active_flows.append(flow_name)
 logger.info(f"Flows triggered: {active_flows}")
 return active_flows