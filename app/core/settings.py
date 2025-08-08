from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='app/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    debug: bool = False
    cors_origin_allowed: list[str] = ['*']
    service_ninjas_api_key: str = 'custom-api-key'
    service_ninjas_url: str = 'https://api.api-ninjas.com/v1/aircraft'


settings = Settings()
