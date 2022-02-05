from pydantic import BaseModel, Field

from app.src.schemas.user import UserModelSchema


class UserSchema(UserModelSchema):
    id_user: int = Field(alias="idUser")


class SearchUserResponse(UserSchema):
    """Response payload for /v1/users GET"""


class CreateUserRequest(BaseModel):
    """Request payload for /v1/users POST"""

    username: str
    email: str


ListUserResponse = list[SearchUserResponse]


class CreateUserResponse(UserSchema):
    """Response payload for /v1/users POST"""


class UpdateUserRequest(BaseModel):
    """Request payload for /v1/users PUT"""

    username: str
    new_email: str = Field(alias="newEmail")


class UpdateUserResponse(UserSchema):
    """Response payload for /v1/users PUT"""
