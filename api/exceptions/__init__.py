from fastapi.exceptions import StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST


class APIException(StarletteHTTPException):
    status_code: int
    message: str

    def __init__(self):
        super(APIException, self).__init__(self.status_code, self.message)


class BadRequestException(APIException):
    status_code = HTTP_400_BAD_REQUEST


class NotFoundException(APIException):
    status_code = HTTP_404_NOT_FOUND
