"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
from random import choice

def rand7() -> int:
    return choice([1, 2, 3, 4, 5, 6, 7])

def rand5() -> int:
    ans = rand7()
    return ans if ans < 6 else rand5()

if __name__ == "__main__":
    d = {}
    for i in range(100):
        a = rand5()
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    
    print(1, ":", d[1])
    print(2, ":",  d[2])
    print(3, ":", d[3])
    print(4, ":", d[4])
    print(5, ":",  d[5])

    