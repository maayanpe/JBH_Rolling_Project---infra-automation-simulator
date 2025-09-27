import os
import logging
from validation import is_valid_vm
from machine import Machine

def to_pos_int(s):
    try:
        n = int(s)
        if n > 0:
            return n
    except:
        pass
    return None

def prompt_one_vm():
    name = input("Enter machine name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        return None

    os_name = input("Enter OS (letters only, e.g. Windows/Linux): ").strip()
    cpu  = to_pos_int(input("Enter CPU (integer > 0): ").strip())
    mem  = to_pos_int(input("Enter Memory (integer > 0): ").strip())
    disk = to_pos_int(input("Enter Disk (integer > 0): ").strip())

    data = {
        "name": name,
        "os": os_name,
        "cpu": cpu if cpu else -1,
        "memory": mem if mem else -1,
        "disk": disk if disk else -1
    }

    ok, msg = is_valid_vm(data)
    if not ok:
        logging.error("Validation failed for '%s': %s", name, msg)
        return {}

    return Machine(data["name"], data["os"], data["cpu"], data["memory"], data["disk"])

def collect_vms():
    items = []
    while True:
        vm = prompt_one_vm()
        if vm is None:
            break
        if vm:
            items.append(vm)
            logging.info("VM accepted: %s", vm.name)
        else:
            logging.info("VM not added (invalid).")
        more = input("Add another machine? (y/n): ").strip().lower()
        if more != "y":
            break
    return items
