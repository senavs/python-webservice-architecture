class APIException(Exception):
    message: str

    def __init__(self):
        super(APIException, self).__init__(self.message)


class BadRequestException(APIException):
    message: str = "Bad Request"


class NotFoundException(APIException):
    message: str = "Not Found"
