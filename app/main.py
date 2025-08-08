from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.exception_handlers import (
    aircraft_not_found_exception_handler,
    aircraft_unknown_error_handler,
)
from app.aircraft_service.custom_exceptions import (
    AircraftNotFoundException,
    AircraftUnknownError,
)


from app.aircraft_service.routes import router as aircraft_router

app = FastAPI(debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_allowed,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_exception_handler(
    AircraftNotFoundException,
    aircraft_not_found_exception_handler  # type: ignore
)
app.add_exception_handler(
    AircraftUnknownError,
    aircraft_unknown_error_handler  # type: ignore
)


@app.get('/health')
async def health() -> dict[str, str]:
    return {'status': 'ok'}


app.include_router(aircraft_router)
