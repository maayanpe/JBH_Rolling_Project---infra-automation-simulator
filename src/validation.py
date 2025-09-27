# src/validation.py
from jsonschema import validate, ValidationError

# Allowed operating systems (lowercase). Extend if you want.
ALLOWED_OSES = {"windows", "win", "linux", "mac", "unix", "centos", "rhel", "ubuntu"}

# Schema to describe what a valid VM must have
VM_SCHEMA = {
    "type": "object",
    "properties": {
        "name":    {"type": "string", "minLength": 1},
        "address": {"type": "string", "minLength": 1},
        "os":      {"type": "string", "minLength": 1},
        "cpu":     {"type": "integer", "minimum": 1},
        "memory":  {"type": "integer", "minimum": 1},
        "disk":    {"type": "integer", "minimum": 1},
    },
    "required": ["name", "address", "os", "cpu", "memory", "disk"],
    "additionalProperties": False,
}

def validate_and_clean(input_data: dict):
    """
    Input: dictionary with VM data
    Output: (ok: bool, valid_data dict or {}, list of error messages)
    """
    errors = []
    valid_data = {}

    # 1) name
    name = str(input_data.get("name") or "").strip()
    if not name:
        errors.append("name: must not be empty")
    else:
        valid_data["name"] = name

    # 2) address
    address = str(input_data.get("address") or "").strip()
    if not address:
        errors.append("address: must not be empty (IP or hostname)")
    else:
        valid_data["address"] = address

    # 3) os
    os_raw = str(input_data.get("os") or "").strip()
    if not os_raw:
        errors.append("os: must not be empty")
    else:
        if not os_raw.isalpha():
            errors.append("os: letters only (A–Z/a–z), no numbers/spaces")
        if os_raw.lower() not in ALLOWED_OSES:
            allowed = ", ".join(sorted(ALLOWED_OSES))
            errors.append(f"os: not allowed. valid values: {allowed}")
        valid_data["os"] = os_raw

    # 4) numeric fields
    for key, label in (("cpu", "CPU"), ("memory", "Memory"), ("disk", "Disk")):
        val = input_data.get(key)
        try:
            value_int = int(str(val).strip())
            if value_int <= 0:
                raise ValueError
            valid_data[key] = value_int
        except Exception:
            errors.append(f"{label}: must be an integer > 0")

    # If errors found, stop here
    if errors:
        return False, {}, errors

    # Final schema check
    try:
        validate(instance=valid_data, schema=VM_SCHEMA)
    except ValidationError as e:
        return False, {}, [f"schema: {e.message}"]

    return True, valid_data, []
