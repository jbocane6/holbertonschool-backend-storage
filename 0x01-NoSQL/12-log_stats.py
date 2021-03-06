#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB:
    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the # of documents in this collection
        second line: Methods:
        5 lines with the number of documents with the method
        ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
        (see example - warning: it's a tabulation before each line)
        one line with the number of documents with:
            method=GET
            path=/status
You can use this dump as data sample: dump.zip
The output of your script must be exactly the same as the README example
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        documents = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {documents}")
    status = mongo_collection.count_documents({"method": "GET",
                                              "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        log_stats(collection)
