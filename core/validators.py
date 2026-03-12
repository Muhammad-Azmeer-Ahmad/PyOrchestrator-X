from pathlib import Path
from core.logger import orchestrator_logger as logger

class TaskValidator:
    def __init__(self, allowed_extensions=None):
        self.allowed_extensions = allowed_extensions or [".py", ".sh"]

    def validate(self, task_path: str) -> bool:
        path = Path(task_path)

        if not path.exists():
            logger.error(f"Task does not exist: {task_path}")
            return False

        if not path.is_file():
            logger.error(f"Task is not a file: {task_path}")
            return False

        if path.suffix not in self.allowed_extensions:
            logger.error(f"Disallowed task type: {path.suffix}")
            return False

        logger.info(f"Task validated: {task_path}")
        return True
