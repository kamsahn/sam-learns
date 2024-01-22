"""
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""


def pigeonhole(arr: list[int]) -> int:
    seen = set()
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,5,6,7,8,9]
    print(pigeonhole(arr))
