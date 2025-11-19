thonfrom src.automation.event_mapper import EventMapper

def test_event_mapping():
 cfg = {
 "event_schema": {"type": str, "user_id": int},
 "mappings": {"signup": {"id": "user_id"}}
 }
 mapper = EventMapper(cfg)
 event = {"type": "signup", "user_id": 123}
 mapped = mapper.map_event(event)
 assert mapped["id"] == 123