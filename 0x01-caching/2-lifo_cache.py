# 2-lifo_cache.py
#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a caching system that follows the LIFO replacement policy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance.
        """
        super().__init__()
        self.last_key = None  # To keep track of the most recent key added.

    def put(self, key, item):
        """
        Add an item in the cache with LIFO eviction policy.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.

        If the cache exceeds BaseCaching.MAX_ITEMS, the last item added
        (LIFO) is discarded.
        """
        if key is None or item is None:
            return

        # Add/Update item in cache
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LIFO: Remove the most recently added item
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]
            self.cache_data[key] = item
        self.last_key = key  # Update last_key to the latest item added

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

