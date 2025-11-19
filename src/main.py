thonfrom fastapi import FastAPI
from automation.event_mapper import EventMapper
from automation.segment_builder import SegmentBuilder
from automation.flow_engine import FlowEngine
from automation.utils.config_loader import load_yaml_config, load_env
from automation.utils.logger import get_logger

app = FastAPI()
logger = get_logger(__name__)

settings = load_yaml_config("config/settings.yaml")
events_cfg = load_yaml_config("config/events.yaml")
segments_cfg = load_yaml_config("config/segments.yaml")
flows_cfg = load_yaml_config("config/flows.yaml")
creds = load_env("config/credentials.env")

event_mapper = EventMapper(events_cfg)
segment_builder = SegmentBuilder(segments_cfg)
flow_engine = FlowEngine(flows_cfg)

@app.get("/health")
def health_check():
 return {"status": "ok"}

@app.post("/event")
def process_event(event: dict):
 logger.info("Incoming event received")
 mapped = event_mapper.map_event(event)
 enriched = segment_builder.build_segments(mapped)
 result = flow_engine.run_flows(enriched)
 return {"processed": True, "result": result}