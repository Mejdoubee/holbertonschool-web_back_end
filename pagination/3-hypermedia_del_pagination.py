#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        Returns a dictionary of paginated data resilient to deletion
        '''
        indexed_dataset = self.indexed_dataset()
        assert (index is None or (0 <= index < len(indexed_dataset)))
        data_page = []
        if index is None:
            index = 0
        keys = sorted(list(indexed_dataset.keys()))
        count = 0
        while count < page_size and keys:
            if index in keys:
                data_page.append(indexed_dataset[index])
                keys.remove(index)
                count += 1
            index += 1
        next_index = index if keys else None

        return {
            'index': next_index - page_size if next_index is not None else 0,
            'data': data_page,
            'page_size': page_size,
            'next_index': next_index
        }
