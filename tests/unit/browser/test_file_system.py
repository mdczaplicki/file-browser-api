from pathlib import Path

import pytest

from file_browser_api.browser import _file_system


@pytest.mark.parametrize(
    ("filename", "expected_result"),
    [
        ("_test_file.txt", "abc\ndef\n123"),
        ("_empty_file.txt", ""),
    ],
)
async def test_read_file__success(filename: str, expected_result: str) -> None:
    # given
    file_path = Path(f"tests/unit/browser/{filename}")

    # when
    result = await _file_system.read_file(file_path)

    # then
    assert result == expected_result


async def test_read_file__missing_file() -> None:
    # given
    file_path = Path("tests/unit/browser/_missing_file.txt")

    # when
    with pytest.raises(FileNotFoundError) as exception_info:
        await _file_system.read_file(file_path)

    # then
    assert "No such file or directory" in str(exception_info.value)
