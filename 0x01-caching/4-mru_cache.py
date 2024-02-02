#!/usr/bin/env python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements the MRU (Most Recently Used) caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """
        Add an item to the cache with MRU policy.
        :param key: Key where the item will be stored.
        :param item: Item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
               key not in self.cache_data:
                if self.most_recent_key:
                    del self.cache_data[self.most_recent_key]
                    print("DISCARD: {}".format(self.most_recent_key))

            self.cache_data[key] = item
            self.most_recent_key = key

    def get(self, key):

        if key is not None and key in self.cache_data:
            self.most_recent_key = key
            return self.cache_data[key]
        return None
