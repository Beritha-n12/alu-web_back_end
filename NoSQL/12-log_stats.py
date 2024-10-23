#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def nginx_logs_stats(mongo_collection):
    """Compute and display stats about Nginx logs."""
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in METHODS}
    for method in METHODS:
        print(f"\tmethod {method}: {method_counts[method]}")

    # Specific method and path count
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_collection = client.logs.nginx

        # Display stats
        nginx_logs_stats(nginx_collection)

    except Exception as e:
        print(f"Error: {e}")
