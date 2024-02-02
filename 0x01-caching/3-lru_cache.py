#!/usr/bin/python3
""" LRU caching module. """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.
    It uses an LRU caching algorithm.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        :param key: Key where the item will be stored.
        :param item: Item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_recently_used_key = self.access_order.pop(0)
                del self.cache_data[least_recently_used_key]
                print("DISCARD: {}".format(least_recently_used_key))

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        :param key: Key that maps to the item in the cache.
        :return: The item stored in the cache or None.
        """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
