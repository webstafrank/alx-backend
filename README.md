1. Caching System Overview
A caching system stores frequently accessed data in memory to improve access speed and reduce the time to retrieve data from slower storage. Caches are limited in size, so they need strategies to determine which items to keep and which to remove when they become full.

2. Cache Replacement Policies Overview
1. FIFO (First-In-First-Out)
Description: Removes the oldest item in the cache when a new item is added and the cache is full.
Implementation: Maintain a list to track the order of insertion and pop the first item when adding a new one.
2. LIFO (Last-In-First-Out)
Description: Removes the most recently added item when a new item is added and the cache is full.
Implementation: Track items in a stack-like structure and pop the last item when adding a new one.
3. LRU (Least Recently Used)
Description: Removes the least recently accessed item when a new item is added, ensuring frequently accessed items remain in the cache.
Implementation: Maintain access order and remove the oldest accessed item.
4. MRU (Most Recently Used)
Description: Removes the most recently accessed item when a new item is added, keeping older items cached longer.
Implementation: Track access and remove the most recently accessed item when needed.
5. LFU (Least Frequently Used)
Description: Removes the item with the lowest access frequency when adding a new item.
Implementation: Track access counts for each item and remove the one with the lowest count.
3. Implementing Cache Classes
Each caching algorithm should be implemented as a separate class that inherits from BaseCaching. Below is a template and sample code for each.

Base Class (BaseCaching) Implementation
The BaseCaching class defines a cache with a maximum size (MAX_ITEMS). When the cache reaches its limit, items are removed according to the cache policy implemented in each derived class.
