#!/usr/bin/env python3
"""
this script will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    ''' returning number via async comperehesion '''
    random_numbers = [number async for number in async_generator()]
    return random_numbers
