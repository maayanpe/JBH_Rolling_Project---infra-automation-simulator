import os
import json
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONF_DIR = os.path.join(BASE_DIR, "configs")
CONF_FILE = os.path.join(CONF_DIR, "instances.json")

def save_instances(vms):
    data = [m.to_dict() for m in vms]
    with open(CONF_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logging.info("Saved %d VM(s) -> %s", len(vms), CONF_FILE)
