"""
There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

# this prompt is offensive


def last_remainder(n: int, k:  int) -> int:
    list_n = list(range(1, n+1))
    i = k-1
    
    while len(list_n) > 1:
        list_n = list_n[:i] + list_n[i+1:]
        i += k-1  # removed one item before the next i
        if i > len(list_n):
            i -= len(list_n) + 1  # loop back to the beginning but add one back since we are starting from the left again
        print(list_n)
    
    return list_n[0]


if __name__ == "__main__":
    print(last_remainder(5, 2))
    print(last_remainder(7, 3))
    # 1, 2, 3, 4, 5, 6, 7
    # 1, 2, 4, 5, 6, 7
    # 1, 2, 3, 5, 7
    # 1, 3, 5, 7
    # 1, 3, 5
    # 1, 3
    # 3
    