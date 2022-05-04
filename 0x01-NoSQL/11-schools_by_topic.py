#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic:
    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic (str) topic searched
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
