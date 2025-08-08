from fastapi import APIRouter, Depends
from typing import Annotated

from app.aircraft_service.schemas import Aircraft, AircraftFullSchema, FatestAircraftSchema
from app.aircraft_service.service import AircarftService


router = APIRouter(prefix='/aircrafts', tags=['aircrafts'])


@router.get('')
async def get_aircrafts(
    manufacturer: str,
    service: Annotated[AircarftService, Depends(AircarftService)],
    limit: int = 30,
) -> list[Aircraft]:
    """Get the list of aircrafts for a specific manufacturer"""

    aircrafts = await service.get_aircraft_by_manufacturer(
        manufacturer=manufacturer, limit=limit
    )

    return aircrafts


@router.get('/{model_name}')
async def get_aircraft(
    model_name: str,
    service: Annotated[AircarftService, Depends(AircarftService)],
) -> AircraftFullSchema:
    """Get the aircraft by model"""

    aircraft = await service.get_aircraft_by_model(model=model_name)

    return aircraft


@router.get('/{manufacturer_name}/fastest')
async def get_fastest_aircraft(
    manufacturer_name: str,
    service: Annotated[AircarftService, Depends(AircarftService)],
    limit: int = 30,
    top_n: int = 5,
) -> list[FatestAircraftSchema]:
    """Get the fastest aircraft for a specific manufacturer"""

    aircrafts = await service.get_fastest_aircraft_by_manufacturer(
        manufacturer=manufacturer_name, limit=limit, top_n=top_n
    )

    return aircrafts
