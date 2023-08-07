#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returning coroutine"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    return [await coroutine for coroutine in asyncio.as_completed(coroutines)]

    """
    for coroutine in asyncio.as_completed(coroutines):
        result = await coroutine
        delays.append(result)

    return delays
    """
