from typing import ClassVar

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    acceptable_modes: ClassVar = 'DEV', 'PROD'

    mode: str
    docs_user: str
    docs_password: str

    model_config = SettingsConfigDict(env_file='.env')
 
    @field_validator('mode')
    @classmethod
    def validate_mode(cls, mode: str) -> str:
        mode = mode.upper()
        if mode not in cls.acceptable_modes:
            raise ValueError()
        return mode


settings = Settings()  # type: ignore[call-arg]
