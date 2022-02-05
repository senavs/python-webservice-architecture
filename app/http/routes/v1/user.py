from fastapi import APIRouter

from app.src.services.user import (
    create_user,
    list_all_users,
    search_user_by_email,
    search_user_by_username,
    update_user_email,
)

from ...payloads.v1.user import (
    CreateUserRequest,
    CreateUserResponse,
    ListUserResponse,
    SearchUserResponse,
    UpdateUserRequest,
    UpdateUserResponse,
)

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", summary="Search for user", response_model=SearchUserResponse)
def _search_user(username: str = None, email: str = None):
    assert bool(username) != bool(email), "select username or email filter, not both and at least one"

    if username:
        return search_user_by_username(username)
    return search_user_by_email(email)


@router.post("/", summary="Create new user", response_model=CreateUserResponse)
def _create_user(body: CreateUserRequest):
    return create_user(username=body.username, email=body.email)


@router.put("/", summary="Update user email", response_model=UpdateUserResponse)
def _update_user(body: UpdateUserRequest):
    return update_user_email(username=body.username, new_email=body.new_email)


@router.get("/all", summary="List all users", response_model=ListUserResponse)
def _list_all_users():
    return list_all_users()
