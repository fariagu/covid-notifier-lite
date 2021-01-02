import pytest
from fastapi.encoders import jsonable_encoder
from backend.app.routes import hello as route
from backend.app.models import hello as model
from backend.app.crud import hello as crud


@pytest.mark.asyncio
@pytest.mark.filterwarnings("ignore::RuntimeWarning")
async def test_add_hello(mocker):
    hello_dict = {
        "message": "mock_message",
        "email": "mock@address.com"
    }
    hello = jsonable_encoder(hello_dict)
    mock_hello = hello

    expected_response = model.ResponseModel(mock_hello, "Hello added successfully")
    actual_response = await route.controller_add_hello(hello)

    assert expected_response == actual_response
