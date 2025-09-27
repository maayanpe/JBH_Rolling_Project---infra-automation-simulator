# src/env_setup.py
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONF_DIR = os.path.join(BASE_DIR, "configs")

def setup_env(log_dir, log_file):
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(CONF_DIR, exist_ok=True)

    # מנקים קונפיג קודם (כדי לא להוסיף handlers כפולים בהרצות נוספות)
    for h in logging.root.handlers[:]:
        logging.root.removeHandler(h)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()  # מציג למסך (אין print)
        ]
    )
    logging.info("Logging ready at %s", log_file)

