#!/usr/bin/env python3
"""Log stats from collection."""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """Provides stats about Nginx logs stored in MongoDB."""
    items = {}
    if option:
        value = mongo_collection.count_documents({"method": {"$regex": option}})
        print(f"\tMethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Run checks
    log_stats(nginx_collection)

    # Additional checks
    print("\nAdditional Checks:")
    print("Check if collection is empty:", nginx_collection.count_documents({}) == 0)
    print("Check if collection has 1 document:", nginx_collection.count_documents({}) == 1)
    print("Check if collection has 10 documents:", nginx_collection.count_documents({}) == 10)
    print("Check if collection has a lot of documents (e.g., >100):", nginx_collection.count_documents({}) > 100)
