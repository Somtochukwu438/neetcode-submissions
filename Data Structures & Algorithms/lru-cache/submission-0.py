from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move key to the end to mark it as recently used
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move key to end
            self.cache[key] = value
            self.queue.remove(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used key
                lru_key = self.queue.popleft()
                del self.cache[lru_key]
            self.cache[key] = value
        self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)