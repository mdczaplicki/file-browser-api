import random
from pathlib import Path

import aiofiles
import pytest

_CURRENT_DIRECTORY = Path(__file__).parent.resolve()

@pytest.fixture
async def random_file_path() -> Path:
    random_name = str(random.randint(100, 999))
    file_path = _CURRENT_DIRECTORY / random_name
    async with aiofiles.open(file_path, "w") as file:
        await file.write(random_name)
    yield file_path
    Path.unlink(file_path)