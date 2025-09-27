# src/validation.py
import re
from jsonschema import validate, ValidationError

ALLOWED_OSES = {"windows", "win", "linux", "mac", "unix", "centos", "rhel"}  # הרחיבי אם תרצי: {"windows","win","linux","ubuntu","centos",...}

VM_SCHEMA = {
    "type": "object",
    "properties": {
        "name":     {"type": "string", "minLength": 1},
        "address":  {"type": "string", "minLength": 1},
        "os":       {"type": "string", "minLength": 1},
        "cpu":      {"type": "integer", "minimum": 1},
        "memory":   {"type": "integer", "minimum": 1},
        "disk":     {"type": "integer", "minimum": 1}
    },
    "required": ["name", "address", "os", "cpu", "memory", "disk"],
    "additionalProperties": False
}

def validate_and_clean(raw: dict):
    """
    מחזיר (ok, cleaned, errors):
      ok - True/False
      cleaned - dict נקי ומוקלד נכון (ints)
      errors - רשימת מחרוזות עם שגיאות לפי שדות (כולל כמה במקביל)
    """
    errors = []
    cleaned = {}

    # name
    name = (raw.get("name") or "").strip()
    if not name:
        errors.append("name: must not be empty")
    else:
        cleaned["name"] = name

    # address
    address = (raw.get("address") or "").strip()
    if not address:
        errors.append("address: must not be empty (IP or hostname)")
    else:
        cleaned["address"] = address

    # os
    os_raw = (raw.get("os") or "").strip()
    if not os_raw:
        errors.append("os: must not be empty")
    else:
        if not re.fullmatch(r"[A-Za-z]+", os_raw):
            errors.append("os: letters only (A–Z/a–z), no numbers/spaces")
        # בדיקת רשימה מותרת (case-insensitive)
        if os_raw.lower() not in ALLOWED_OSES:
            allowed = ", ".join(sorted(ALLOWED_OSES))
            errors.append(f"os: not allowed. valid values: {allowed}")
        cleaned["os"] = os_raw

    # numeric fields
    for fld, label in [("cpu", "CPU"), ("memory", "Memory"), ("disk", "Disk")]:
        val = raw.get(fld)
        try:
            iv = int(str(val).strip())
            if iv <= 0:
                raise ValueError
            cleaned[fld] = iv
        except Exception:
            errors.append(f"{label}: must be an integer > 0")

    if errors:
        return False, {}, errors

    # סכימה רשמית (שקטה) לשמירת הדרישה
    try:
        validate(instance=cleaned, schema=VM_SCHEMA)
    except ValidationError as e:
        errors.append(f"schema: {e.message}")
        return False, {}, errors

    return True, cleaned, []

