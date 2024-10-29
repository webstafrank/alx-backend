# 3-lru_cache.py
#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system that follows the LRU replacement policy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain LRU order

    def put(self, key, item):
        """
        Add an item in the cache with LRU eviction policy.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, the least recently used
        item is discarded.
        """
        if key is None or item is None:
            return

        # If key exists, update the item and move it to end to mark as most recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LRU: Remove the least recently used item (first item)
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            self.cache_data.pop(oldest_key)

        # Add new item or update existing item and mark as most recently used
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            The value associated with key if it exists, or None if key is
            None or not present in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move accessed item to end to mark as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

