#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except task_wait_random
is being called.
"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(coroutines):
        result = await completed_task
        delays.append(result)

    return delays
