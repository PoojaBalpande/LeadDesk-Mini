class ApplicationError(Exception):
    """Base exception for all LeadDesk Mini domain and system errors."""
    def __init__(self, message: str = "An application error occurred.") -> None:
        self.message = message
        super().__init__(self.message)
