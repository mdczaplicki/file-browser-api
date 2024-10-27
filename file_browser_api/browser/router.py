from pathlib import Path

from fastapi import APIRouter

from file_browser_api.browser import controller
from file_browser_api.browser.schema import CreateFilePayload
from file_browser_api.settings import FILE_BROWSER_API_SETTINGS

FILE_ROUTER = APIRouter()
DIRECTORY_ROUTER = APIRouter()

@FILE_ROUTER.get("/")
async def read_file(file_path: str) -> str:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary /file_path
    return await controller.read_file(path)


@FILE_ROUTER.put("/")
async def update_file(file_path: str, content: str) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.update_file(path, content)

@FILE_ROUTER.delete("/")
async def delete_file(file_path: str) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.delete_file(path)

@FILE_ROUTER.post("/")
async def create_file(file_path: str, payload: CreateFilePayload) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.create_file(path, payload.content)

@DIRECTORY_ROUTER.get("/")
async def list_directory(directory_path : str) -> list[str]:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / directory_path
    return await controller.list_directory(path)