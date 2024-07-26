from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

mongodb_uri = getenv("MONGODB_URI")

if not mongodb_uri:
    raise ValueError("No MONGODB_URI found in environment variables")

# Local database
#db_client = MongoClient().local

# Remote database
db_client = MongoClient(mongodb_uri).test