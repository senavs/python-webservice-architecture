from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse


def validation_error(_: Request, exception: RequestValidationError) -> JSONResponse:
    errors = [
        {"location": validation._loc[0], "name": validation._loc[1], "message": str(validation.exc)}
        for validation in exception.args[0]
    ]
    return JSONResponse(status_code=422, content=errors)
