"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def nth_perfect(n: int):
    return int(str(n) + str(10 - n)) if 0 < n < 10 else None


if __name__ == "__main__":
    print(nth_perfect(0))
    print(nth_perfect(1))
    print(nth_perfect(2))
    print(nth_perfect(3))
    print(nth_perfect(4))
    print(nth_perfect(5))
    print(nth_perfect(6))
    print(nth_perfect(7))
    print(nth_perfect(8))
    print(nth_perfect(9))
    print(nth_perfect(10))
    print(nth_perfect(11))
