#!/usr/bin/env python3
"""Defines a class for interacting with Redis"""

from functools import wraps
import redis
from typing import Any, Callable, Union, Optional
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator for counting and caching the number of calls to `method`"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        obj = args[0]
        obj._redis.incrby(method.__qualname__)
        ret = method(*args, **kwargs)
        return ret

    return wrapper


class Cache:
    """Contains methods for interacting with a redis database"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Returns the value stored with `key`.
        The variable is decoded using the function `fn`
        """
        data = self._redis.get(key)

        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Returns a string stored with `key`"""
        return self.get(key, fn=lambda s: s.decode())

    def get_int(self, key: str) -> int:
        """Returns an integerr stored with `key`"""
        return self.get(key, fn=lambda s: int(s.decode()))
