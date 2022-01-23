from fastapi import APIRouter

from ...payloads.v1.user import CreateUserResponse, CreateUserRequest
from ...services.user import create_user, search_user

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", summary="Create new user", response_model=CreateUserResponse)
def _search_user(username: str = None, email: str = None):
    return search_user(username=username, email=email)


@router.post("/", summary="Create new user", response_model=CreateUserResponse)
def _create_user(body: CreateUserRequest):
    return create_user(username=body.username, email=body.email)
