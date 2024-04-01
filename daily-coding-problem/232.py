"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""

class PrefixMapSum:
    def __init__(self):
        self.store = dict()
    
    def insert(self, key: str, value: int):
        self.store[key] = value
        
    def sum(self, key: str) -> int:
        ans = 0
        for k, v in self.store.items():
            if k[:len(key)] == key:
                ans += v
        return ans


if __name__ == "__main__":
    pms = PrefixMapSum()
    pms.insert("columnar", 2)
    print(pms.sum("col"))
    
    pms.insert("row", 4)
    print(pms.sum("col"))
    
    pms.insert("column", 3)
    print(pms.sum("col"))
