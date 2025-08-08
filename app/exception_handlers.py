from fastapi.responses import JSONResponse
from fastapi import Request
from app.aircraft_service.custom_exceptions import (
    AircraftNotFoundException,
    AircraftUnknownError,
)


async def aircraft_not_found_exception_handler(
    request: Request, exc: AircraftNotFoundException
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.message},
    )


async def aircraft_unknown_error_handler(
    request: Request, exc: AircraftUnknownError
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={'message': exc.message},
    )
