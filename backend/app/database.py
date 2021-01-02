from motor import motor_asyncio
import os

db_container_name = os.environ.get('DB_CONTAINER_NAME')
db_container_port = os.environ.get('DB_CONTAINER_PORT')

MONGO_DETAILS = f"mongodb://{db_container_name}:{db_container_port}"

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.covid_notifier

hello_collection = database.get_collection("hello_collection")
covid_collection = database.get_collection("covid_collection")
