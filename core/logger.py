import logging
import sys
from pathlib import Path


def get_logger(module_name="Orchestrator"):
    """
    Creates a standardized logger for PyOrchestratorX.
    Outputs to both 'logs/orchestrator.log' and the terminal.
    """
    logger = logging.getLogger(module_name)

    # Prevent duplicate handlers if get_logger is called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    # Format: Timestamp | Task/Module | Status Level | Message
    # Example: 2023-10-27 10:00:00 | [Recon] | INFO | Starting scan...
    formatter = logging.Formatter(
        '%(asctime)s | [%(name)s] | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # --- Setup Paths ---
    # Finds the root directory (PyOrchestratorX) relative to this file
    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "logs"
    log_file = log_dir / "orchestrator.log"

    # Ensure the log directory exists (failsafe)
    log_dir.mkdir(exist_ok=True)

    # --- Handlers ---

    # 1. Console Handler (Standard Output)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)  # High-level info for the user
    logger.addHandler(console_handler)

    # 2. File Handler (Persistent Audit Log)
    try:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)  # Catch everything (errors, debug info)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"CRITICAL: Logging to file failed. Error: {e}")

    return logger


# --- Task Status Helper ---
def log_task(logger, task_name, status, message=""):
    """
    A specific helper to standardize 'Fiverr Proof' logs.
    Usage: log_task(log, "API_RECON", "START", "Target: google.com")
    """
    status_msg = f"STATUS: {status} | {message}"
    logger.info(status_msg)


# Default logger instance
orchestrator_logger = get_logger("System")

if __name__ == "__main__":
    # Test block to verify it works
    orchestrator_logger.info("Logger initialized successfully.")
    log_task(orchestrator_logger, "Self-Test", "SUCCESS", "Logger is ready for production.")