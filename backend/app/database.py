from dotenv import load_dotenv
from motor import motor_asyncio
import os
import urllib

load_dotenv()

db_username = os.environ.get('DB_USERNAME')
db_password = urllib.parse.quote(os.environ.get('DB_PASSWORD'))
db_container_name = os.environ.get('DB_CONTAINER_NAME')
db_container_port = os.environ.get('DB_CONTAINER_PORT')

MONGO_DETAILS = f"mongodb://{db_username}:{db_password}@{db_container_name}:{db_container_port}/?authSource=admin&readPreference=primary&ssl=false"

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.covid_notifier

hello_collection = database.get_collection("hello_collection")
covid_collection = database.get_collection("covid_collection")
