# src/input_handler.py
import logging
from validation import validate_and_clean
from machine import Machine

def prompt_one_vm():

    logging.info("--- Collect VM data ---")

    name    = input("Enter machine name: ").strip()
    address = input("Enter machine address (IP/Hostname): ").strip()
    os_name = input("Enter OS (letters only, e.g. Windows/Linux): ").strip()
    cpu     = input("Enter CPU (integer > 0): ").strip()
    mem     = input("Enter Memory (integer > 0): ").strip()
    disk    = input("Enter Disk (integer > 0): ").strip()

    return {
        "name": name,
        "address": address,
        "os": os_name,
        "cpu": cpu,
        "memory": mem,
        "disk": disk,
    }

def collect_vms():
    items = []
    while True:
        raw_vm = prompt_one_vm()

        ok, cleaned, errs = validate_and_clean(raw_vm)
        if ok:
            vm = Machine(
                cleaned["name"],
                cleaned["address"],
                cleaned["os"],
                cleaned["cpu"],
                cleaned["memory"],
                cleaned["disk"],
            )
            items.append(vm)
            logging.info("VM %d accepted: %s (%s)", len(items), vm.name, vm.address)
        else:
            logging.error("Validation failed for VM input:")
            for e in errs:
                logging.error("  - %s", e)
            logging.info("VM not added (invalid).")

        more = input("Add another machine? (y/n): ").strip().lower()
        if more != "y":
            break

    return items
