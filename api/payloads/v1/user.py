from pydantic import BaseModel

from ...schemas.user import UserModelSchema


class CreateUserRequest(BaseModel):
    """Request payload for /v1/users/ POST"""

    username: str
    email: str


class CreateUserResponse(UserModelSchema):
    """Response payload for /v1/users/ POST"""
