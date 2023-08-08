#!/usr/bin/env python3
'''
 this script will execute async_comprehension four times in parallel
 using asyncio.gather.
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    ''' running async_comprehension four times '''
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = asyncio.get_event_loop().time()
    final = end - start
    return final
