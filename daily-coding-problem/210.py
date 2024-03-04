"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


def collatz(n: int, c: int = 0) -> tuple:
    c += 1
    if n == 1:
        return 1, c
    if n % 2 == 0:
        return collatz(n // 2, c)
    else:
        return collatz((3*n)+1, c)


def find_max_collatz() -> tuple:
    # total_c = 0
    max_c = 0
    max_i = 0
    for i in range(1, 1000001):
        _, c = collatz(i)
        # total_c += c
        if c > max_c:
            max_c = c
            max_i = i

    # print(total_c)
    return max_i, max_c


if __name__ == "__main__":
    # print(collatz(1))
    print(find_max_collatz())
