import random
from contextlib import suppress
from pathlib import Path

import aiofiles.os
import pytest

_STUBS_DIRECTORY = Path(__file__).parent.resolve() / "stubs"


@pytest.fixture
async def random_file_path() -> Path:
    random_name = str(random.randint(100, 999))
    file_path = _STUBS_DIRECTORY / random_name
    async with aiofiles.open(file_path, "w") as file:
        await file.write(random_name)
    yield file_path
    with suppress(FileNotFoundError):
        await aiofiles.os.remove(file_path)
