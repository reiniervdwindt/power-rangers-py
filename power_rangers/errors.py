__all__ = [
    'PowerRangersException',
    'BadRequestException',
    'UnauthorizedException',
    'ForbiddenException',
    'NotFoundException'
]


class PowerRangersException(BaseException):
    """Base Exception type for trakt module"""
    http_code = message = None

    def __str__(self):
        return self.message


class BadRequestException(PowerRangersException):
    """
    PowerRangersException type to be raised when a 401 return code is received
    """
    http_code = 400
    message = "Bad Request"


class UnauthorizedException(PowerRangersException):
    """
    PowerRangersException type to be raised when a 401 return code is received
    """
    http_code = 401
    message = 'Unauthorized'


class ForbiddenException(PowerRangersException):
    """
    PowerRangersException type to be raised when a 403 return code is received
    """
    http_code = 403
    message = 'Forbidden'


class NotFoundException(PowerRangersException):
    """
    PowerRangersException type to be raised when a 404 return code is received
    """
    http_code = 404
    message = 'Not Found'
