# src/input_handler.py
import logging
from validation import validate_and_clean
from machine import Machine

def prompt_one_vm():
    logging.info("--- Provisioning: collect VM data ---")
    name    = input("Enter machine name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        return None

    address = input("Enter machine address (IP/Hostname): ").strip()
    os_name = input("Enter OS (letters only, e.g. Windows/Linux): ").strip()
    cpu     = input("Enter CPU (integer > 0): ").strip()
    mem     = input("Enter Memory (integer > 0): ").strip()
    disk    = input("Enter Disk (integer > 0): ").strip()

    ok, cleaned, errs = validate_and_clean({
        "name": name,
        "address": address,
        "os": os_name,
        "cpu": cpu,
        "memory": mem,
        "disk": disk
    })

    if not ok:
        # לוג ברור לכל שגיאה
        logging.error("Validation failed for VM input:")
        for e in errs:
            logging.error("  - %s", e)
        return {}  # לא נוסיף לרשימה

    logging.info("Validation OK for VM '%s' (%s)", cleaned["name"], cleaned["address"])
    return Machine(
        cleaned["name"],
        cleaned["address"],
        cleaned["os"],
        cleaned["cpu"],
        cleaned["memory"],
        cleaned["disk"],
    )

def collect_vms():
    items = []
    idx = 0
    while True:
        vm = prompt_one_vm()
        if vm is None:
            break
        if vm:
            idx += 1
            items.append(vm)
            logging.info("VM %d accepted: %s (%s)", idx, vm.name, vm.address)
        else:
            logging.info("VM not added (invalid).")
        more = input("Add another machine? (y/n): ").strip().lower()
        if more != "y":
            break
    return items

