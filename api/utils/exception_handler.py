from sanic.exceptions import SanicException
from sanic.response import json
from http import *

class BadRequestException(SanicException):
    def __init__(self, message):
        super().__init__(message, HTTPStatus.BAD_REQUEST)


async def handle_exception(request, exception):
    return json({'message': str(exception)}, status=exception.status_code)
