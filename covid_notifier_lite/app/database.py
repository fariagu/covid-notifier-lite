from motor import motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.covid_notifier

hello_collection = database.get_collection("hello_collection")
covid_collection = database.get_collection("covid_collection")