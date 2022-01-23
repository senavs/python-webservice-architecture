from . import NotFoundException, BadRequestException


class UserNotFoundError(NotFoundException):
    message = "user information not found"


class UserAlreadyRegisterError(BadRequestException):
    message = "user already register with (username or email)"
