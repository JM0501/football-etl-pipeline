from pymongo import MongoClient, UpdateOne
from config.settings import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def upsert_documents(collection_name: str, data: list, key: str):
    collection = db[collection_name]
    operations = [
        UpdateOne({key: doc[key]}, {"$set": doc}, upsert=True)
        for doc in data
    ]
    if operations:
        result = collection.bulk_write(operations)
        print(f"{collection_name}: Inserted={result.upserted_count}, Updated={result.modified_count}")
    else:        print(f"No documents to upsert in {collection_name}.")