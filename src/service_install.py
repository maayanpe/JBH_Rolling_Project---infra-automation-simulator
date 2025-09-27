# src/service_install.py
import os
import logging
import subprocess

# Project paths
project_dir = os.path.dirname(os.path.dirname(__file__))
script_path = os.path.join(project_dir, "scripts", "install_service.sh")
log_path = os.path.join(project_dir, "logs", "provisioning.log")

def run_install_for_vm(machine_address, service_name):
    logging.info("Start install on %s (service=%s)", machine_address, service_name)

    # Add LOG_PATH for the bash script
    environment = os.environ.copy()
    environment["LOG_PATH"] = log_path

    try:
        # Run the script, collect output, do not print to screen
        result = subprocess.run(
            [script_path, machine_address, service_name],
            text=True,
            capture_output=True,
            env=environment
        )

        # Log what the script wrote
        if result.stdout:
            logging.info("bash stdout: %s", result.stdout.strip())
        if result.stderr:
            logging.error("bash stderr: %s", result.stderr.strip())

        # Check exit code
        if result.returncode != 0:
            logging.error("Install failed on %s (exit=%s)", machine_address, result.returncode)
        else:
            logging.info("Install finished OK on %s", machine_address)

    except Exception as error:
        logging.exception("Failed to run install script on %s: %s", machine_address, error)
