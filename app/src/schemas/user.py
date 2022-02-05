from . import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str


class UserModelSchema(UserSchema):
    id_user: int
