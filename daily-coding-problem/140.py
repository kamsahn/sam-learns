"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

def two_only_once(arr: list[int]) -> list[int]:
    store = {}
    for i in arr:
        if store.get(i):
            # if we've already seen it, remove from store
            del store[i]
        else:
            store[i] = 1

    keys = [k for k in store.keys()]
    # ensure we only have two keys
    assert len(keys) == 2
    return keys

if __name__ == "__main__":
    print(two_only_once([2, 4, 6, 8, 10, 2, 6, 10]))
