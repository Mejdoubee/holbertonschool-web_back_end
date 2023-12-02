#!/usr/bin/env python3
'''
Module to create an asyncio.Task using wait_random.
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Create an asyncio Task based on wait_random coroutine
    '''
    return asyncio.create_task(wait_random(max_delay))
