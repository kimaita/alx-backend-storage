#!/usr/bin/env python3
"""Queries and displays some data from mongoDB"""

from pymongo import MongoClient


def method_count(collection, http_methods):
    """Returns a count for each method in http_methods"""
    pipeline = [
        {"$match": {"method": {"$in": http_methods}}},
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
    ]
    return collection.aggregate(pipeline)


def get_count(collection):
    """Returns the number of GET documents with path as '/status'"""
    return collection.count_documents(
        {
            "$and": [
                {"method": "GET"},
                {"path": "/status"},
            ]
        }
    )


def main():
    """Connects to the mongoDB database and generates a report on nginx logs"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {m["_id"]: m["count"] for m in method_count(collection, methods)}
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {counts.get(method) or 0}")

    print(f"{get_count(collection)} status check")


if __name__ == "__main__":
    main()
