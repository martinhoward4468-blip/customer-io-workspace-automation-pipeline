thondef validate_schema(data, schema):
 for key, expected_type in schema.items():
 if key not in data:
 raise ValueError(f"Missing field: {key}")
 if not isinstance(data[key], expected_type):
 raise ValueError(f"Invalid type for {key}: expected {expected_type}")