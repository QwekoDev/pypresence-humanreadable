class HumanReadableException(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = 'An unknown error has occured.'
        super().__init__(message)


class InvalidTime(HumanReadableException):
    def __init__(self, message: str):
        super().__init__(message)


class BadArgument(HumanReadableException):
    def __init__(self, received, expected):
        super().__init__("Expected type {} but got {} instead.".format(expected, received))
