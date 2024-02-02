#!/usr/bin/env python3

from base_caching import BaseCaching
import time


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    Implements the LFU (Least Frequently Used) caching algorithm.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_frequency = {}
        self.key_access_time = {}

    def put(self, key, item):
        """
        Add an item to the cache with LFU policy.
        :param key: Key where the item will be stored.
        :param item: Item to store in the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
               key not in self.cache_data:
                self.discard()

            self.cache_data[key] = item
            self.key_frequency[key] = self.key_frequency.get(key, 0) + 1
            self.key_access_time[key] = self.current_time()

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        :param key: Key that maps to the item in the cache.
        :return: The item stored in the cache or None.
        """
        if key is not None and key in self.cache_data:
            self.key_frequency[key] += 1
            self.key_access_time[key] = self.current_time()
            return self.cache_data[key]
        return None

    def current_time(self):
        """
        Get the current time for tracking access time.
        """
        return time.time()

    def discard(self):
        """
        Discard an item from the cache using LFU algorithm.
        If multiple items have the same frequency, use LRU.
        """
        if not self.cache_data:
            return

        # Find the least frequently used key
        lfu_key = min(self.key_frequency,
                      key=lambda k: (self.key_frequency[k],
                                     self.key_access_time[k]))
        del self.cache_data[lfu_key]
        del self.key_frequency[lfu_key]
        del self.key_access_time[lfu_key]
        print("DISCARD: {}".format(lfu_key))
