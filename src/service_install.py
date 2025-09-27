import os
import logging
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCRIPT_FILE = os.path.join(BASE_DIR, "scripts", "install_service.sh")
LOG_FILE = os.path.join(BASE_DIR, "logs", "provisioning.log")

def run_install(service):
    env = os.environ.copy()
    env["LOG_PATH"] = LOG_FILE
    try:
        res = subprocess.run([SCRIPT_FILE, service], text=True, capture_output=True, env=env)
        if res.returncode != 0:
            logging.error("Service install failed: %s", res.stderr.strip())
        else:
            logging.info("Service install finished: %s", service)
            if res.stdout.strip():
                logging.info("Script output: %s", res.stdout.strip())
    except Exception as e:
        logging.exception("Failed running bash script: %s", e)
