from pathlib import Path

import aiofiles.os


async def read_file(file_path: Path) -> str:
    async with aiofiles.open(file_path, "r") as file:
        file_content = await file.read()
    return file_content

async def save_file(file_path: Path, content: str) -> None:
    async with aiofiles.open(file_path, "w") as file:
        await file.write(content)