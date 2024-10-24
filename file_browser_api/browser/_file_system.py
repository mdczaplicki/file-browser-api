from pathlib import Path

import aiofiles.os


async def read_file(file_path: Path) -> str:
    async with aiofiles.open(file_path) as file:
        file_content = await file.read()
    return file_content


async def save_file(file_path: Path, content: str) -> None:
    async with aiofiles.open(file_path, "w") as file:
        await file.write(content)


async def delete_file(file_path: Path) -> None:
    await aiofiles.os.remove(file_path)


async def list_directory(directory_path: Path) -> list[str]:
    directory_content = await aiofiles.os.listdir(directory_path)
    return directory_content


async def does_file_exist(file_path: Path) -> bool:
    exists = await aiofiles.os.path.exists(file_path)
    return exists
