from typing import Any
from bson.objectid import ObjectId
from app.database import hello_collection

#helpers
def hello_helper(hello) -> dict:
    return {
        "id": str(hello["_id"]),
        "message": hello["message"],
        "email": hello["email"]
    }


async def add_hello(hello_data: dict) -> dict:
    """
    Add a new hello to the database
    """
    hello = await hello_collection.insert_one(hello_data)
    new_hello = await hello_collection.find_one({"_id": hello.inserted_id})
    return hello_helper(new_hello)


async def get_hello(id: str) -> dict:
    """
    Get a hello with a given ID
    """
    hello = await hello_collection.find_one({"_id": ObjectId(id)})
    if hello:
        return hello_helper(hello)


async def get_all_helloes() -> Any:
    """
    Get all helloes in the database
    """
    helloes = []
    async for hello in hello_collection.find():
        helloes.append(hello_helper(hello))

    return helloes


async def update_hello(id: str, data: dict) -> bool:
    """
    Update a hello with a matching ID
    """
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    hello = await hello_collection.find_one({"_id": ObjectId(id)})
    if hello:
        updated_hello = await hello_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_hello:
            return True

        return False


async def delete_hello(id: str) -> bool:
    """
    Delete a hello from the database
    """
    hello = await hello_collection.find_one({"_id": ObjectId(id)})
    if hello:
        await hello_collection.delete_one({"_id": ObjectId(id)})
        return True
    
    return False