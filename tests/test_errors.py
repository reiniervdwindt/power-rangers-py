import unittest

from power_rangers.errors import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException
)


class ErrorsTestCase(unittest.TestCase):
    def test_bad_request(self):
        error = BadRequestException()
        self.assertEqual(error.http_code, 400)
        self.assertEqual(str(error), 'Bad Request')

    def test_unauthorized(self):
        error = UnauthorizedException()
        self.assertEqual(error.http_code, 401)
        self.assertEqual(str(error), 'Unauthorized')

    def test_forbidden(self):
        error = ForbiddenException()
        self.assertEqual(error.http_code, 403)
        self.assertEqual(str(error), 'Forbidden')

    def test_not_found(self):
        error = NotFoundException()
        self.assertEqual(error.http_code, 404)
        self.assertEqual(str(error), 'Not Found')
