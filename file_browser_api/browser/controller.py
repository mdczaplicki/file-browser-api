from pathlib import Path

from file_browser_api.browser import _file_system
from file_browser_api.browser.error import FileNotFoundBrowserError, NotADirectoryBrowserError


async def read_file(file_path: Path) -> str:
    try:
        content = await _file_system.read_file(file_path)
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(file_path) from ex
    return content


async def update_file(file_path: Path, content: str) -> None:
    file_exists = await _file_system.does_file_exist(file_path)
    if not file_exists:
        raise FileNotFoundBrowserError(file_path)
    await _file_system.save_file(file_path, content)


async def delete_file(file_path: Path) -> None:
    try:
        await _file_system.delete_file(file_path)
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(file_path) from ex


async def create_file(file_path: Path, content: str) -> None:
    await _file_system.save_file(file_path, content)


async def list_directory(directory_path: Path) -> list[str]:
    try:
        directory_content = await _file_system.list_directory(directory_path)
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(directory_path) from ex
    except NotADirectoryError as ex:
        raise NotADirectoryBrowserError(directory_path) from ex
    return directory_content
