import logging
from fastapi.exceptions import RequestValidationError

from handlers.tools.message import Error as err, Ok as ok


logger = logging.getLogger("task_manager")

class BaseError(Exception):
    def __init__(self, error_text: str):
        self.error_text = error_text
        self.callback()

    def callback(self):
        print(f"{self.__class__.__name__}: {self.error_text}")
        return err


class TaskUserError(BaseError):
    pass

class TaskError(BaseError):
    pass

class UserError(BaseError):
    pass

