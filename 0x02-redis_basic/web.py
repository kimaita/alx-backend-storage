#!/usr/bin/env python3
"""Contains functions for tracking requests for a page"""

import requests
import redis
from functools import wraps


def track_calls(func):
    """Counts each request to get a requested page."""

    @wraps(func)
    def wrapper(*args):
        r = redis.Redis(decode_responses=True)
        key = f"count:{args[0]}"
        r.incr(key)
        r.expire(key, 10, nx=True)
        ret = func(*args)
        return ret

    return wrapper


@track_calls
def get_page(url: str) -> str:
    """Gets and returns the HTML content of the page at `url`

    Args
        url(str)

    Returns
        the url's HTML content
    """
    r = requests.get(url)
    return r.text
