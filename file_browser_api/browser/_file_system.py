from pathlib import Path

import aiofiles.os

from file_browser_api.browser.error import FileNotFoundBrowserError, NotADirectoryBrowserError


async def read_file(file_path: Path) -> str:
    try:
        async with aiofiles.open(file_path) as file:
            file_content = await file.read()
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(file_path) from ex
    return file_content


async def save_file(file_path: Path, content: str) -> None:
    async with aiofiles.open(file_path, "w") as file:
        await file.write(content)


async def delete_file(file_path: Path) -> None:
    try:
        await aiofiles.os.remove(file_path)
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(file_path) from ex


async def list_directory(directory_path: Path) -> list[str]:
    try:
        directory_content = await aiofiles.os.listdir(directory_path)
    except FileNotFoundError as ex:
        raise FileNotFoundBrowserError(directory_path) from ex
    except NotADirectoryError as ex:
        raise NotADirectoryBrowserError(directory_path) from ex
    return directory_content


async def does_file_exist(file_path: Path) -> bool:
    exists = await aiofiles.os.path.exists(file_path)
    return exists
