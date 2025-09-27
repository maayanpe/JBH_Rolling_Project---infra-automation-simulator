# infra-automation-simulator

## 1. Overview
A beginner-friendly infrastructure automation simulator. **No real installs are performed**—all provisioning and service installation steps are simulated for safe experimentation.

## 2. Requirements & Install
- Python 3.7+
- Install dependencies (uses `jsonschema` for validation):
- pip install -r requirements.txt

## 3. Run
Start the simulator:
python -m src.infra_simulator

## 4. Project Structure
infra-automation-simulator/ ├── src/ │   ├── infra_simulator.py │   ├── env_setup.py │   ├── input_handler.py │   ├── validation.py │   ├── provision.py │   ├── machine.py ├── scripts/ │   └── install_service.sh ├── requirements.txt


## 5. How it works
- **Input Loop:** The simulator prompts for VM details in a `while True` loop, allowing you to add multiple machines interactively.
- **Validation Rules:** Inputs are validated (type, allowed OS, positive integers) using both custom logic and `jsonschema`. Invalid entries are rejected with error messages.
- **JSON Output Path:** All VM instances are saved to `configs/instances.json` after collection.
- **Calling Bash with LOG_PATH:** Service installation is simulated by calling `scripts/install_service.sh` for each VM, passing the machine address and service name. The script uses the `LOG_PATH` environment variable to write logs.
- **Logging:** All actions and errors are logged to `logs/provisioning.log` and also shown in the console.

## 6. Troubleshooting
- **Permissions:** If you get a permission error running the shell script, use:
chmod +x scripts/install_service.sh

or call it via `bash scripts/install_service.sh ...`.
- **Line Endings:** On Windows, convert scripts to LF (Unix) using `dos2unix` if you see issues with CRLF.
- **ModuleNotFoundError:** Run the simulator with `-m`:
python -m src.infra_simulator

- **Missing `jsonschema`:** Make sure you installed requirements:
pip install -r requirements.txt


---
Simulation only—no real infrastructure is changed.

