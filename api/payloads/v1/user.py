from pydantic import BaseModel

from ...schemas.user import UserModelSchema


class SearchUserResponse(UserModelSchema):
    """Response payload for /v1/users GET"""


class CreateUserRequest(BaseModel):
    """Request payload for /v1/users POST"""

    username: str
    email: str


class CreateUserResponse(UserModelSchema):
    """Response payload for /v1/users POST"""


class UpdateUserRequest(BaseModel):
    """Request payload for /v1/users PUT"""

    username: str
    new_email: str


class UpdateUserResponse(UserModelSchema):
    """Response payload for /v1/users PUT"""
