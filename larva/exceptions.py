class LarvaException(Exception):
    def __repr__(self):
        return self.message


class AuthenticationFailureError(LarvaException):
    pass


class NoUsernameGivenError(LarvaException):
    pass


class NoURLGivenError(LarvaException):
    pass


class CommandNotAvailableError(LarvaException):
    pass
