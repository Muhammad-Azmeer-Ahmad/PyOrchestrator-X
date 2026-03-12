from core.validators import validate_command


class CommandSecurityError(Exception):
    """Custom exception raised when a command violates security policies."""
    pass


class CommandGuard:
    @staticmethod
    def execute_safely(raw_command: str):
        """
        The entry point for any command execution.
        Validates the command and prepares it for the subprocess.
        """
        try:
            # 1. Consult the validators
            sanitized_parts = validate_command(raw_command)

            # 2. If it passes, return the parts for subprocess execution
            # Logging the attempt is highly recommended here
            print(f"[SECURITY] Command approved: {sanitized_parts[0]}")
            return sanitized_parts

        except ValueError as e:
            # 3. Block and Raise
            # We wrap the ValueError in a more specific Security Error
            error_msg = f"SECURITY ALERT: Blocked execution attempt -> {str(e)}"
            print(f"[BLOCK] {error_msg}")
            raise CommandSecurityError(error_msg)