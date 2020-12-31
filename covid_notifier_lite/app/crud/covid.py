from typing import Any
from bson.objectid import ObjectId
from covid_notifier_lite.app.database import covid_collection


#helpers
def covid_helper(covid) -> dict:
    return {
        "id": str(covid["_id"]),
        "report_no": covid["report_no"],
        "download_url": covid["download_url"]
    }

async def add_covid(covid_data: dict) -> dict:
    """
    Add a new covid to the database
    """
    covid = await covid_collection.insert_one(covid_data)
    new_covid = await covid_collection.find_one({"_id": covid.inserted_id})
    return covid_helper(new_covid)


async def get_covid(id: str) -> dict:
    """
    Get a covid with a given ID
    """
    covid = await covid_collection.find_one({"_id": ObjectId(id)})
    if covid:
        return covid_helper(covid)

async def get_covid_by_report_no(report_no: str) -> dict:
    """
    Get a covid with a given report number
    """
    covid = await covid_collection.find_one({"report_no": report_no})
    if covid:
        return covid_helper(covid)


async def get_all_covids() -> Any:
    """
    Get all covids in the database
    """
    covids = []
    async for covid in covid_collection.find():
        covids.append(covid_helper(covid))

    return covids


async def update_covid(id: str, data: dict) -> bool:
    """
    Update a covid with a matching ID
    """
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    covid = await covid_collection.find_one({"_id": ObjectId(id)})
    if covid:
        updated_covid = await covid_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_covid:
            return True

        return False


async def delete_covid(id: str) -> bool:
    """
    Delete a covid from the database
    """
    covid = await covid_collection.find_one({"_id": ObjectId(id)})
    if covid:
        await covid_collection.delete_one({"_id": ObjectId(id)})
        return True
    
    return False