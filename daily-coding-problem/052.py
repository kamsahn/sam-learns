"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

# keys are stored in dict
# order stored in list


class LRU:
    def __init__(self, n: int):
        self.size = n
        self.store = {}
        self.order = []

    def c_set(self, key, value):
        if len(self.order) == self.size:
            removed = self.order.pop(0)
            del self.store[removed]

        self.order.append(key)
        self.store[key] = value
    
    def c_get(self, key):
        res = self.store.get(key, None)
        
        if res:
            self.order.remove(key)
            self.order.append(key)

        return res


if __name__ == "__main__":
    lru = LRU(3)
    print(lru.order)
    lru.c_set("foo", "bar")
    print(lru.order)
    lru.c_set("fizz", "buzz")
    print(lru.order)
    lru.c_set("wee", "woo")
    print(lru.order)
    print("value at fizz:", lru.c_get("fizz"))
    print(lru.order)
    print("value at wow:", lru.c_get("wow"))
    print(lru.order)
    lru.c_set("gee", "wizz")
    print(lru.order)
    print("value at foo:", lru.c_get("foo"))
    print(lru.order)
    print("value at gee:", lru.c_get("gee"))
    print(lru.order)


        
        