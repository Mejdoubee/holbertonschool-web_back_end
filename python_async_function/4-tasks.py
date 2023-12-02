#!/usr/bin/env python3
'''
Module to run wait_random multiple times concurrently using asyncio Tasks.
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawns wait_random n times with the specified max_delay
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
