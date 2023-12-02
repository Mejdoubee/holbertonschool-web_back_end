#!/usr/bin/env python3
'''
This module provides a function to sum a list of integers and floats.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats as argument and returns their sum as a float.
    '''
    return sum(mxd_lst)
