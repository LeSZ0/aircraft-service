
import pytest
from unittest.mock import AsyncMock, patch

from app.aircraft_service.service import AircarftService
from app.aircraft_service.custom_exceptions import AircraftNotFoundException


@pytest.mark.asyncio
@patch("app.aircraft_service.service.AircarftService._make_request", new_callable=AsyncMock)
async def test_get_aircraft_by_manufacturer(mock_make_request: AsyncMock) -> None:
    """Test case for the get_aircraft_by_manufacturer method"""

    mock_make_request.return_value = [
        {
            "manufacturer": "Boeing",
            "model": "747",
            "engine_type": "Jet",
            "max_speed_knots": "570",
            "gross_weight_lbs": "970000",
            "length_ft": "231",
            "height_ft": "63"
        }
    ]

    service = AircarftService()
    aircrafts = await service.get_aircraft_by_manufacturer(manufacturer="Boeing")

    assert len(aircrafts) == 1
    assert aircrafts[0].manufacturer == "Boeing"


@pytest.mark.asyncio
@patch("app.aircraft_service.service.AircarftService._make_request", new_callable=AsyncMock)
async def test_get_aircraft_by_model(mock_make_request: AsyncMock) -> None:
    """Test case for the get_aircraft_by_model method"""

    mock_make_request.return_value = [
        {
            "manufacturer": "Boeing",
            "model": "747",
            "engine_type": "Jet",
            "max_speed_knots": "570",
            "gross_weight_lbs": "970000",
            "length_ft": "231",
            "height_ft": "63"
        }
    ]

    service = AircarftService()
    aircraft = await service.get_aircraft_by_model(model="747")

    assert aircraft.model == "747"


@pytest.mark.asyncio
@patch("app.aircraft_service.service.AircarftService._make_request", new_callable=AsyncMock)
async def test_get_aircraft_by_model_not_found(mock_make_request: AsyncMock) -> None:
    """Test case for the get_aircraft_by_model method when the aircraft is not found"""

    mock_make_request.return_value = []

    service = AircarftService()
    with pytest.raises(AircraftNotFoundException):
        await service.get_aircraft_by_model(model="747")


@pytest.mark.asyncio
@patch("app.aircraft_service.service.AircarftService._make_request", new_callable=AsyncMock)
async def test_get_fastest_aircraft_by_manufacturer(mock_make_request: AsyncMock) -> None:
    """Test case for the get_fastest_aircraft_by_manufacturer method"""

    mock_make_request.return_value = [
        {
            "manufacturer": "Boeing",
            "model": "747",
            "engine_type": "Jet",
            "max_speed_knots": "570",
            "gross_weight_lbs": "970000",
            "length_ft": "231",
            "height_ft": "63"
        },
        {
            "manufacturer": "Boeing",
            "model": "777",
            "engine_type": "Jet",
            "max_speed_knots": "590",
            "gross_weight_lbs": "775000",
            "length_ft": "242",
            "height_ft": "61"
        }
    ]

    service = AircarftService()
    aircrafts = await service.get_fastest_aircraft_by_manufacturer(manufacturer="Boeing")

    assert len(aircrafts) == 2
    assert aircrafts[0].model == "777"
