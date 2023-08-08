#!/usr/bin/env python3
import asyncio
import random
""" this script defines async generator """


async def async_generator():
    """ generating iterable """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
