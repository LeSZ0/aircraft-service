import pytest
from unittest.mock import patch, AsyncMock
from types import MappingProxyType

from fastapi.testclient import TestClient

from app.main import app
from app.aircraft_service.schemas import Aircraft, AircraftFullSchema, FatestAircraftSchema

MPH_CONVERSION_RATE = 1.15078
MAX_SPEED_KNOTS = 590


COMMON_AIRCRAFT_DATA = MappingProxyType({
    'manufacturer': 'Boeing',
    'model': '747',
    'engine_type': 'Jet',
    'max_speed_knots': '590',
    'max_speed_miles_per_hour': str(round(MAX_SPEED_KNOTS * MPH_CONVERSION_RATE)),
    'gross_weight_lbs': '970000',
    'length_ft': '231',
    'height_ft': '63',
})

COMMON_AIRCRAFT_777_DATA = MappingProxyType({
    'manufacturer': 'Boeing',
    'model': '777',
    'engine_type': 'Jet',
    'max_speed_knots': '590',
    'max_speed_miles_per_hour': str(round(MAX_SPEED_KNOTS * MPH_CONVERSION_RATE)),
    'gross_weight_lbs': '775000',
    'length_ft': '242',
    'height_ft': '61',
})

HTTP_200_OK = 200


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@patch(
    'app.aircraft_service.service.AircarftService.get_aircraft_by_manufacturer'
)
def test_get_aircrafts(mock_get_aircrafts: AsyncMock, client: TestClient) -> None:
    """Test case for the get_aircrafts endpoint"""

    mock_get_aircrafts.return_value = [Aircraft(**COMMON_AIRCRAFT_DATA)]

    response = client.get('/aircrafts?manufacturer=Boeing')

    aircrafts_response_data = MappingProxyType({
        'manufacturer': 'Boeing',
        'model': '747',
        'engine_type': 'Jet',
        'max_speed_kt': '590',
        'max_speed_mph': str(round(MAX_SPEED_KNOTS * MPH_CONVERSION_RATE)),
        'gross_weight_lbs': '970000',
        'length_ft': '231',
        'height_ft': '63',
    })

    assert response.status_code == HTTP_200_OK
    assert response.json() == [aircrafts_response_data]


@patch('app.aircraft_service.service.AircarftService.get_aircraft_by_model')
def test_get_aircraft(mock_get_aircraft: AsyncMock, client: TestClient) -> None:
    """Test case for the get_aircraft endpoint"""

    mock_get_aircraft.return_value = AircraftFullSchema(**COMMON_AIRCRAFT_777_DATA)

    response = client.get('/aircrafts/747')

    aircraft_777_response_data = MappingProxyType({
        'manufacturer': 'Boeing',
        'model': '777',
        'engine_type': 'Jet',
        'max_speed_kt': '590',
        'max_speed_mph': str(round(MAX_SPEED_KNOTS * MPH_CONVERSION_RATE)),
        'gross_weight_lbs': '775000',
        'length_ft': '242',
        'height_ft': '61',
        'ceiling_ft': None,
        'cruise_speed_knots': None,
        'empty_weight_lbs': None,
        'landing_ground_roll_ft': None,
        'range_nautical_miles': None,
        'rate_of_climb_ft_per_min': None,
        'takeoff_ground_run_ft': None,
        'wing_span_ft': None,
    })

    assert response.status_code == HTTP_200_OK
    assert response.json() == aircraft_777_response_data


@patch(
    'app.aircraft_service.service.AircarftService.get_fastest_aircraft_by_manufacturer'
)
def test_get_fastest_aircraft(mock_get_fastest_aircraft: AsyncMock, client: TestClient) -> None:
    """Test case for the get_fastest_aircraft endpoint"""

    mock_get_fastest_aircraft.return_value = [
        FatestAircraftSchema(**COMMON_AIRCRAFT_777_DATA)
    ]

    response = client.get('/aircrafts/Boeing/fastest')

    fastest_aircraft_response_data = MappingProxyType({
        'manufacturer': 'Boeing',
        'model': '777',
        'engine_type': 'Jet',
        'max_speed_kt': '590',
        'max_speed_mph': str(round(MAX_SPEED_KNOTS * MPH_CONVERSION_RATE)),
    })

    assert response.status_code == HTTP_200_OK
    assert response.json() == [fastest_aircraft_response_data]
