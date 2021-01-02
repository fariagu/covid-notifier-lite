import pytest
from backend.app.app import read_root


@pytest.mark.asyncio
async def test_root():
    expectedMessage = { "message": "Hello World of Covid"}
    message = await read_root()

    assert expectedMessage == message
