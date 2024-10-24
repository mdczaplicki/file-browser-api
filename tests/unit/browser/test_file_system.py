from pathlib import Path

import aiofiles
import pytest

from file_browser_api.browser import _file_system

_CURRENT_DIRECTORY = Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    ("filename", "expected_result"),
    [
        ("_test_file.txt", "abc\ndef\n123"),
        ("_empty_file.txt", ""),
    ],
)
async def test_read_file(filename: str, expected_result: str) -> None:
    # given
    file_path = _CURRENT_DIRECTORY / filename

    # when
    result = await _file_system.read_file(file_path)

    # then
    assert result == expected_result


async def test_read_file__missing_file() -> None:
    # given
    file_path = _CURRENT_DIRECTORY / "_missing_file.txt"

    # when
    with pytest.raises(FileNotFoundError) as exception_info:
        await _file_system.read_file(file_path)

    # then
    assert "No such file or directory" in str(exception_info.value)

@pytest.mark.parametrize("new_content", ["", "abc", "abc\ndef", "\0"])
async def test_save_file(random_file_path: Path, new_content: str) -> None:
    # when
    await _file_system.save_file(random_file_path, new_content)

    # then
    async with aiofiles.open(random_file_path, "r") as updated_file:
        content = await updated_file.read()

    assert content == new_content