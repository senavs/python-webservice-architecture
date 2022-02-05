from starlette.requests import Request
from starlette.responses import JSONResponse


def assertion_error(_: Request, exception: AssertionError) -> JSONResponse:
    return JSONResponse(status_code=400, content={"message": str(exception)})
