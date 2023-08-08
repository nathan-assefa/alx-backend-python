#!/usr/bin/env python3
import asyncio
import random
from typing import Generator


""" this script defines async generator """


async def async_generator() -> Generator[float, None, None]:
    """ generating iterable """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
