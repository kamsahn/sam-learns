"""
Implement an LFU (Least Frequently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value.
If there are already n items in the cache and we are adding a new item,
then it should also remove the least frequently used item.
If there is a tie, then the least recently used key should be removed.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""
import time


class Item:
    def __init__(self, value: any):
        self.value = value
        self.counter = 0
        self.ts = time.time()


class LFU:
    def __init__(self, n: int):
        self.size = n
        self.store = {}
    
    def set(self, key: any, value: any):
        store = self.store
        new_item = Item(value)
        deleted = None
        
        if len(store) >= self.size:
            lfu_keys = []
            low = 9999  # high number
            for i in store:
                if store[i].counter < low:
                    low = store[i].counter
                    lfu_keys = [i]
                elif store[i].counter == low:
                    lfu_keys.append(i)
            
            if len(lfu_keys) == 1:
                del store[lfu_keys[0]]
                deleted = lfu_keys[0]
            else:
                least_recent_ts = time.time()
                least_recent_key = None
                
                for i in lfu_keys:
                    if store[i].ts < least_recent_ts:
                        least_recent_ts = store[i].ts
                        least_recent_key = i
                
                del store[least_recent_key]
                deleted = least_recent_key
        
        store[key] = new_item  # account for key clash
        print("added k/v:", key, value)
        if deleted:
            print("deleted key:", deleted)
    
    def get(self, key) -> any:
        item = self.store[key]
        item.counter += 1
        item.ts = time.time()
        print("retrieved k/v:", key, item.value)
        return item.value


if __name__ == "__main__":
    lfu = LFU(3)
    lfu.set(1, "one")
    lfu.set(2, "two")
    lfu.get(1)
    lfu.get(2)
    lfu.set(3, "three")
    lfu.set(4, "four")
    lfu.set(5, "five")
    lfu.get(5)
    lfu.set(6, "six")

    
                        
                    
                
        
        
