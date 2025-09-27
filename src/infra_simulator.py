# src/infra_simulator.py
import os
import logging
from env_setup import setup_env
from input_handler import collect_vms
from provision import save_instances
from service_install import run_install_for_vm

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "provisioning.log")

def main():
    setup_env(LOG_DIR, LOG_FILE)
    logging.info("=== Start provisioning session ===")

    vms = collect_vms()
    save_instances(vms)

    if vms:
        logging.info("Starting service installation (simulated) for all VMs...")
        for m in vms:
            run_install_for_vm(m.address, "nginx")

    logging.info("=== End provisioning session ===")

if __name__ == "__main__":
    main()

