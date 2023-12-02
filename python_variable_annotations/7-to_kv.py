#!/usr/bin/env python3
'''
This module provides a function to generate
a tuple from a string and a number (int or float).
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function to_kv that takes a string k and an int OR float v as arguments
    and returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v and is a float.
    '''
    return (k, float(v**2))
