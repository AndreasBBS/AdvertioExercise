class FooterError(Exception):
    """Base class for exceptions related to the Footer Class"""
    def __init__(self, message):
        """Constructor"""
        super().__init__()
        self.message = message
