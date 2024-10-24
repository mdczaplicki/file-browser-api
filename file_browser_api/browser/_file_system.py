from pathlib import Path

import aiofiles


async def read_file(file_path: Path) -> str:
    async with aiofiles.open(file_path) as file:
        file_content = await file.read()
    return file_content
