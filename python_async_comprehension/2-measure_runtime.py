#!/usr/bin/env python3
'''
Module for measuring runtime of the async_comprehension coroutine
'''
import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of the async_comprehension coroutine
    executed four times in parallel.
    '''
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()

    return end_time - start
