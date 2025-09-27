import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONF_DIR = os.path.join(BASE_DIR, "configs")

def setup_env(log_dir, log_file):
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(CONF_DIR, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )
    logging.info("Logging ready at %s", log_file)
