"""
Given an integer n and a list of integers l,
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

from random import choice

def random_number(n: int, l: list) -> int:
    return choice([e for e in range(n) if e not in l])

if __name__ == "__main__":
    ans = {}
    for _ in range(100):
        a = random_number(10, [4, 5, 6])
        if ans.get(a):
            ans[a] += 1
        else:
            ans[a] = 1
    sorted_ans = {}
    for k, v in sorted(ans.items()):
        sorted_ans[k] = v
    print(sorted_ans)
