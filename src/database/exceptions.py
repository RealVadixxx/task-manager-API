class DBError(Error):
    def __init__(self, error_text: str):
        self.error_text = error_text
        self.message = "DB Error"
        super().__init__(f"{self.message}: {self.error}")