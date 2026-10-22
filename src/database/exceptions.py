class BaseError(Exception):
    def __init__(self, error_text: str):
        self.error_text = error_text
        self.callback()

    def callback(self):
        print(f"{self.__class__.__name__}: {self.error_text}")
        return err

class DBError(BaseError):
    pass