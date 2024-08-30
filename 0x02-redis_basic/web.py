#!/usr/bin/env python3
"""Contains functions for tracking requests for a page"""

import requests
import redis
from functools import wraps

r = redis.Redis(decode_responses=True)


def track_calls(func):
    """Counts each request to get a requested page."""

    @wraps(func)
    def wrapper(*args):
        key = f"count:{args[0]}"
        r.incr(key)
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
    cached = r.get(url)
    if cached:
        return cached

    resp = requests.get(url)
    html = resp.text
    r.set(url, html, ex=10)

    return html
