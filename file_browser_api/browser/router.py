from collections.abc import AsyncGenerator

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from file_browser_api.browser import controller
from file_browser_api.browser.error import FileNotFoundBrowserError, NotADirectoryBrowserError
from file_browser_api.browser.schema import CreateFilePayload
from file_browser_api.settings import FILE_BROWSER_API_SETTINGS

FILE_ROUTER = APIRouter()
DIRECTORY_ROUTER = APIRouter()


async def _raise_404_on_file_not_found_error() -> AsyncGenerator:
    try:
        yield
    except FileNotFoundBrowserError as ex:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "File not found") from ex


async def _raise_400_on_not_a_dictionary_error() -> AsyncGenerator:
    try:
        yield
    except NotADirectoryBrowserError as ex:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Not a directory") from ex


@FILE_ROUTER.get("/", dependencies=[Depends(_raise_404_on_file_not_found_error)])
async def read_file(file_path: str) -> str:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    return await controller.read_file(path)


@FILE_ROUTER.put("/", dependencies=[Depends(_raise_404_on_file_not_found_error)])
async def update_file(file_path: str, content: str) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.update_file(path, content)


@FILE_ROUTER.delete("/", dependencies=[Depends(_raise_404_on_file_not_found_error)])
async def delete_file(file_path: str) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.delete_file(path)


@FILE_ROUTER.post("/", status_code=status.HTTP_201_CREATED)
async def create_file(file_path: str, payload: CreateFilePayload) -> None:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / file_path
    await controller.create_file(path, payload.content)


@DIRECTORY_ROUTER.get(
    "/", dependencies=[Depends(_raise_404_on_file_not_found_error), Depends(_raise_400_on_not_a_dictionary_error)]
)
async def list_directory(directory_path: str = "") -> list[str]:
    path = FILE_BROWSER_API_SETTINGS.main_dictionary / directory_path
    return await controller.list_directory(path)
