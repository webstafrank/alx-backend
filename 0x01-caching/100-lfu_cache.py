# 100-lfu_cache.py
#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache defines a caching system with the LFU algorithm.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}  # Track the usage frequency of each key

    def put(self, key, item):
        """
        Add an item in the cache with LFU eviction policy.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, the least frequently used
        item is discarded. If there is a tie, the least recently used item is
        discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item and increment usage frequency
            self.cache_data.move_to_end(key)
            self.usage_frequency[key] += 1
        else:
            # If cache is full, remove the LFU (or LRU if tie) item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k in self.cache_data if self.usage_frequency[k] == min_freq]

                # Remove the least recently used of the least frequently used items
                lfu_key = lfu_keys[0]
                print(f"DISCARD: {lfu_key}")
                self.cache_data.pop(lfu_key)
                del self.usage_frequency[lfu_key]

            # Add new item and set initial usage frequency
            self.cache_data[key] = item
            self.usage_frequency[key] = 1

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

        # Increment usage frequency and mark as recently used
        self.usage_frequency[key] += 1
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

