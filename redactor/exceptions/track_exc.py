

class LooperException(Exception):
    def __init__(self, msg):
        self.message = msg


class OccupiedException(LooperException):
    pass


class TimeCannotBeZero(LooperException):
    pass

