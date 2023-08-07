#!/usr/bin/env python3
"""
********* Steps to solve the answer **********
- Import the required modules.
- Define the measure_time function that takes n and max_delay as arguments.
- Measure the start time using time.time().
- Call the wait_n() function with the provided n and max_delay arguments.
- Measure the end time using time.time().
- Calculate the total execution time by subtracting the start time from
  the end time.
- Return the average execution time per task by dividing the total
  execution time by n.
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returning float"""
    start_time = time.time()

    # Asynchronously run the wait_n function and await the results.
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_execution_time = end_time - start_time

    return total_execution_time / n
