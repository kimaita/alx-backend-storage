#!/usr/bin/env python3
"""Defines a class for interacting with Redis"""

import redis
from typing import Union
import uuid


class Cache:
    """Contains methods for interacting with a redis database"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis using a random key.

        Args:
            data -  the variable to store

        Returns:
            str - the key associated with data in redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
