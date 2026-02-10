import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    # Test: list collections (should be empty if new)
    collections = db.list_collection_names()
    print(f"Connected to database '{MONGO_DB_NAME}'. Collections: {collections}")
except Exception as e:
    print("Could not connect to MongoDB:", e)
