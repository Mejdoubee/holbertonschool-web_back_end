#!/usr/bin/env python3
'''
This module provides a function to get the length of each element in a list.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Takes an iterable of sequences and returns a list of tuples, where each
    tuple contains an element from the input and its length.
    '''
    return [(i, len(i)) for i in lst]
