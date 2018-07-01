class FooterError(Exception):
    """Base class for exceptions Related to the Footer Class"""
    def __init__(self, message):
        super().__init__()
        self.message = message