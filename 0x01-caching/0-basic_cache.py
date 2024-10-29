# 0-basic_cache.py
#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a basic caching system without a limit on stored items.
    Inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item to the cache_data dictionary with the provided key.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from cache_data using the given key.

        Args:
            key (str): The key to look up in cache_data.

        Returns:
            The value associated with key if it exists, or None if key is
            None or not present in cache_data.
        """
        return self.cache_data.get(key, None)

