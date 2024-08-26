#!/usr/bin/env python3
"""Contains a function for listing MongoDB documents"""

def list_all(mongo_collection):
    """"""
    return mongo_collection.find({})
