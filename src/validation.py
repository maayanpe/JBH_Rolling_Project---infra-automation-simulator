
from jsonschema import validate, ValidationError

VM_SCHEMA = {
    "type": "object",
    "properties": {
        "name":   {"type": "string", "minLength": 1},
        "os":     {"type": "string", "pattern": "^[A-Za-z]+$"},
        "cpu":    {"type": "integer", "minimum": 1},
        "memory": {"type": "integer", "minimum": 1},
        "disk":   {"type": "integer", "minimum": 1}
    },
    "required": ["name", "os", "cpu", "memory", "disk"],
    "additionalProperties": False
}

def is_valid_vm(d):
    try:
        validate(instance=d, schema=VM_SCHEMA)
        return True, ""
    except ValidationError as e:
        return False, str(e.message)
