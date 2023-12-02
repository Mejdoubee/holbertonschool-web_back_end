#!/usr/bin/env python3
'''
This module provides a function to generate a multiplier function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    '''
    def multiplier_func(x: float) -> float:
        '''
        Internal function to multiply a given number by the external multiplier
        '''
        return x * multiplier
    return multiplier_func
