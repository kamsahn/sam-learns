"""
Suppose you have a multiplication table that is N by N.
That is, a 2D array where the value at the i-th row and j-th column
is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X,
write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""

# for each int n within N,
# if (X / n) % 1 == 0 and (X / n) <= N
# (is an integer and less than or equal to N)
# add one to the count


def times_in_table(N: int, X: int) -> int:
    count = 0
    for i in range(N):
        r = X / (i+1)
        if r % 1 == 0 and r <= N:
            count += 1
    return count


if __name__ == "__main__":
    print(times_in_table(6, 12))  # 4
    print(times_in_table(6, 10))  # 2
    print(times_in_table(6, 9))  # 1
    print(times_in_table(4, 20))  # 0
    print(times_in_table(6, 20))  # 2



            