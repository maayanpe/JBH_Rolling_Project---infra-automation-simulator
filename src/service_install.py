# src/service_install.py
import os
import logging
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCRIPT_FILE = os.path.join(BASE_DIR, "scripts", "install_service.sh")
LOG_FILE = os.path.join(BASE_DIR, "logs", "provisioning.log")

def run_install_for_vm(machine_addr, service):
    logging.info("Service install started for %s (service=%s)", machine_addr, service)
    env = os.environ.copy()
    env["LOG_PATH"] = LOG_FILE  # אם תרצי שהbash יכתוב גם ללוג הזה
    try:
        res = subprocess.run([SCRIPT_FILE, machine_addr, service],
                             text=True, capture_output=True, env=env)
        if res.stdout.strip():
            logging.info("bash stdout: %s", res.stdout.strip())
        if res.stderr.strip():
            logging.error("bash stderr: %s", res.stderr.strip())

        if res.returncode != 0:
            logging.error("Service install failed on %s (exit=%s)", machine_addr, res.returncode)
        else:
            logging.info("Service install finished OK on %s", machine_addr)
    except Exception as e:
        logging.exception("Failed running bash script for %s: %s", machine_addr, e)

