#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def nginx_logs_stats(mongo_collection):
    """Compute and display stats about Nginx logs."""
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs where x is the number of documents in this collection")

    # Methods count
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\t{count} {method} requests")

    # Specific method and path count
    specific_log_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"1 GET /status request: {specific_log_count}")

if __name__ == "__main__":
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_collection = client.logs.nginx

        # Display stats
        nginx_logs_stats(nginx_collection)

    except Exception as e:
        print(f"Error: {e}")
