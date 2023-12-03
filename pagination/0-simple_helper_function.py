#!/usr/bin/env python3
'''
A module to compute the index range for pagination.
'''


def index_range(page, page_size):
    '''
    Calculate the start and end index for a given page and page size
    '''
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx
