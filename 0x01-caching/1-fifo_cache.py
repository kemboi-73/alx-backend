#!/usr/bin/env python3
""" FIFO caching module. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache.
        :param key: Key where the item will be stored.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        return self.cache_data.get(key, None)
