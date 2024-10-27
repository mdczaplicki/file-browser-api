from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class _FileBrowserAPISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="file_browser_api_")

    _main_directory: str  # = Field(alias="file_browser_api_main_directory")

    @property
    def main_dictionary(self):
        return Path(self._main_directory)

FILE_BROWSER_API_SETTINGS = _FileBrowserAPISettings()