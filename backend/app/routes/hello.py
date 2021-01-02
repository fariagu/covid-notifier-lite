from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.app.crud.hello import (
    add_hello,
    get_hello,
    get_all_helloes,
    update_hello,
    delete_hello
)

from backend.app.models.hello import (
    ErrorResponseModel,
    ResponseModel,
    HelloSchema,
    UpdateHelloModel
)

HelloRouter = APIRouter()

@HelloRouter.post("/", response_description="Add hello data to database")
async def controller_add_hello(hello: HelloSchema = Body(...)):
    hello = jsonable_encoder(hello)
    new_hello = await add_hello(hello)
    return ResponseModel(new_hello, "Hello added successfully")

@HelloRouter.get("/", response_description="Get all helloes from database")
async def controller_get_all_helloes():
    helloes = await get_all_helloes()
    return ResponseModel(helloes, "Retrived Hello data")
