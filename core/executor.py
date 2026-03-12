import subprocess
from pathlib import Path
from core.logger import orchestrator_logger as logger
from core.validators import TaskValidator


class Executor:
    """
    Executes automation tasks safely using validator and logs all activity.
    """

    def __init__(self, validator: TaskValidator):
        self.validator = validator

    def run(self, task_path: str):
        """
        Validate and execute a task script.
        :param task_path: path to Python (.py) or Shell (.sh) script
        """
        task_file = Path(task_path)

        # Step 1: Validate task
        if not self.validator.validate(task_path):
            logger.error(f"Task validation failed: {task_path}")
            return

        logger.info(f"Starting task: {task_path}")

        # Step 2: Determine command based on file type
        if task_file.suffix == ".py":
            cmd = ["python3", str(task_file)]
        elif task_file.suffix == ".sh":
            cmd = ["bash", str(task_file)]
        else:
            logger.error(f"Unsupported task type: {task_file.suffix}")
            return

        # Step 3: Execute command safely
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )

            logger.info(f"Task completed successfully: {task_path}")
            if result.stdout:
                logger.info(f"Output:\n{result.stdout.strip()}")

        except subprocess.CalledProcessError as e:
            logger.error(f"Task failed with error:\n{e.stderr.strip() if e.stderr else str(e)}")

        except Exception as e:
            logger.error(f"Unexpected error while executing task: {str(e)}")
