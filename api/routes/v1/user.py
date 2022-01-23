from fastapi import APIRouter

from ...payloads.v1.user import (
    CreateUserResponse,
    CreateUserRequest,
    UpdateUserRequest,
    UpdateUserResponse,
    SearchUserResponse,
)
from ...services.user import create_user, search_user, update_user_email

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", summary="Search for user", response_model=SearchUserResponse)
def _search_user(username: str = None, email: str = None):
    return search_user(username=username, email=email)


@router.post("/", summary="Create new user", response_model=CreateUserResponse)
def _create_user(body: CreateUserRequest):
    return create_user(username=body.username, email=body.email)


@router.put("/", summary="Update user email", response_model=UpdateUserResponse)
def _update_user(body: UpdateUserRequest):
    return update_user_email(username=body.username, new_email=body.new_email)
