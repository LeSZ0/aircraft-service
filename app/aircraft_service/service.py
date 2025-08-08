import httpx
from typing import Any
from starlette.status import HTTP_404_NOT_FOUND

from app.core.settings import settings
from app.aircraft_service.schemas import Aircraft, AircraftFullSchema, FatestAircraftSchema
from app.aircraft_service.custom_exceptions import (
    AircraftNotFoundException,
    AircraftUnknownError,
)


class AircarftService:
    """Service layer to interact with the external API"""

    def __init__(self, endpoint_name: str = '/aircraft') -> None:
        self.endpoint_name = endpoint_name
        self.api_key = settings.service_ninjas_api_key
        self.endpoint = f'{settings.service_ninjas_url}{endpoint_name}'

    async def get_aircraft_by_manufacturer(
        self, manufacturer: str, limit: int = 30
    ) -> list[Aircraft]:
        """Get the list of aircrafts for a specific manufacturer"""

        request_params = {'manufacturer': manufacturer, 'limit': limit}
        response_data = await self._make_request(request_params)

        return [
            Aircraft.model_validate(aircraft_data)
            for aircraft_data in response_data
        ]

    async def get_aircraft_by_model(self, model: str) -> AircraftFullSchema:
        """Get the aircraft by model"""
        request_params = {'model': model}
        response_data = await self._make_request(request_params)
        if not response_data:
            raise AircraftNotFoundException()

        return AircraftFullSchema.model_validate(response_data[0])

    async def get_fastest_aircraft_by_manufacturer(
        self, manufacturer: str, limit: int = 30, top_n: int = 5
    ) -> list[FatestAircraftSchema]:
        """Get the fastest aircraft for a specific manufacturer"""

        aircrafts = await self.get_aircraft_by_manufacturer(
            manufacturer=manufacturer, limit=limit
        )

        if not aircrafts:
            return []

        top_n = min(top_n, len(aircrafts))

        sorted_data = sorted(
            aircrafts,
            key=lambda aircraft: aircraft.max_speed_knots,
            reverse=True,
        )[:top_n]

        return [
            FatestAircraftSchema.model_validate(aircraft_data.model_dump())
            for aircraft_data in sorted_data
        ]

    async def _make_request(
        self, request_params: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Private method to make a request to the API and return the response.

        The intention of this method is to avoid code duplication
        """
        try:
            async with httpx.AsyncClient() as client:
                headers = {'X-Api-Key': self.api_key}
                response = await client.get(
                    self.endpoint, params=request_params, headers=headers
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exception:
            if exception.response.status_code == HTTP_404_NOT_FOUND:
                raise AircraftNotFoundException()
            else:
                raise AircraftUnknownError()
