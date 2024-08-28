#!/usr/bin/env python3
""""""

import requests
import redis
from functools import wraps


def track_calls(func):
    """Counts each request to get a requested page."""

    @wraps(func)
    def wrapper(*args):
        r = redis.Redis(decode_responses=True)
        key = f"count:{args[0]}"
        ret = func(*args)
        r.incrby(key)
        r.expire(key, 10, nx=True)
        return ret

    return wrapper


@track_calls
def get_page(url: str) -> str:
    """"""
    r = requests.get(url)
    return r.text
