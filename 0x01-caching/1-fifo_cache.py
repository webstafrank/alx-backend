# 1-fifo_cache.py
#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a caching system that follows the FIFO replacement policy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance.
        """
        super().__init__()
        self.order = []  # List to maintain the order of keys for FIFO.

    def put(self, key, item):
        """
        Add an item in the cache with FIFO eviction policy.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, the first item added
        (FIFO) is discarded.
        """
        if key is None or item is None:
            return

        # Add/Update item in cache
        if key in self.cache_data:
            self.order.remove(key)  # Remove key if it already exists in the order
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # FIFO: Remove the oldest item
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)  # Add key to end of order list

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            The value associated with key if it exists, or None if key is
            None or not present in the cache.
        """
        return self.cache_data.get(key, None)

