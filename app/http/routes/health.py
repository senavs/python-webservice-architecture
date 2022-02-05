from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(tags=["Health"])


@router.get("/health", summary="API health check")
def _check():
    return PlainTextResponse("ok")
