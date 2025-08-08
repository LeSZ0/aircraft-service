from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Any

MPH_CONVERSION_RATE = 1.15078


class Aircraft(BaseModel):
    manufacturer: str = Field(alias='manufacturer')
    model: str = Field(...)
    engine_type: str = Field(...)
    max_speed_knots: str = Field(alias='max_speed_kt')
    max_speed_miles_per_hour: str = Field(alias='max_speed_mph')
    gross_weight_lbs: str = Field(...)
    length_ft: str = Field(...)
    height_ft: str = Field(...)

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode="before")
    def calculate_max_speed_miles_per_hour(cls, model_data: dict[Any, Any]) -> dict[Any, Any]:
        max_speed_knots = float(model_data['max_speed_knots'])
        max_speed_miles_per_hour = str(round(max_speed_knots * MPH_CONVERSION_RATE))
        model_data['max_speed_miles_per_hour'] = max_speed_miles_per_hour
        return model_data


class AircraftFullSchema(BaseModel):
    manufacturer: str = Field(alias='manufacturer')
    model: str = Field(...)
    engine_type: str = Field(...)
    max_speed_knots: str = Field(alias='max_speed_kt')
    max_speed_miles_per_hour: str | None = Field(alias='max_speed_mph', default=None)
    cruise_speed_knots: str | None = Field(default=None)
    ceiling_ft: str | None = Field(default=None)
    rate_of_climb_ft_per_min: str | None = Field(default=None)
    takeoff_ground_run_ft: str | None = Field(default=None)
    landing_ground_roll_ft: str | None = Field(default=None)
    gross_weight_lbs: str | None = Field(default=None)
    empty_weight_lbs: str | None = Field(default=None)
    length_ft: str | None = Field(default=None)
    height_ft: str | None = Field(default=None)
    wing_span_ft: str | None = Field(default=None)
    range_nautical_miles: str | None = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode="before")
    def calculate_max_speed_miles_per_hour(cls, model_data: dict[Any, Any]) -> dict[Any, Any]:
        max_speed_knots = float(model_data['max_speed_knots'])
        max_speed_miles_per_hour = str(round(max_speed_knots * MPH_CONVERSION_RATE))
        model_data['max_speed_miles_per_hour'] = max_speed_miles_per_hour
        return model_data


class FatestAircraftSchema(BaseModel):
    manufacturer: str = Field(alias='manufacturer')
    model: str = Field(...)
    engine_type: str = Field(...)
    max_speed_knots: str = Field(alias='max_speed_kt')
    max_speed_miles_per_hour: str = Field(alias='max_speed_mph')

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode="before")
    def calculate_max_speed_miles_per_hour(cls, model_data: dict[Any, Any]) -> dict[Any, Any]:
        max_speed_knots = float(model_data['max_speed_knots'])
        max_speed_miles_per_hour = str(round(max_speed_knots * MPH_CONVERSION_RATE))
        model_data['max_speed_miles_per_hour'] = max_speed_miles_per_hour
        return model_data
