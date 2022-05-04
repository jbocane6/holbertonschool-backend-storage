#!/usr/bin/env python3
"""
Python function that changes all topics of a school document
based on the name
  Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name(str) school name to update
        topics(str list) list of topics approached in the school
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
