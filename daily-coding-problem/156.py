"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""

# for i in n to 0, if i^2 is less than n
# add j, where j is in i to 0 where i^2 + j^2 <= n
# recure


def smallest_num_squared(n: int, ans: list) -> int:
    for i in range(n, 0, -1):
        if i*i <= n:
            if n - sum(ans) >= i*i:
                ans.append(i*i)
                print(ans)
                if sum(ans) == n:
                    return len(ans)
                return smallest_num_squared(n, ans)


if __name__ == "__main__":
    print(smallest_num_squared(13, []))
    print(smallest_num_squared(27, []))
    print(smallest_num_squared(28, []))
    print(smallest_num_squared(29, []))
