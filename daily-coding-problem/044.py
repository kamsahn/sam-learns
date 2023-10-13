"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
uniform probability, implement a function rand7() that returns an integer from
1 to 7 (inclusive).
"""

import random


def rand5():
    return random.choice([1,2,3,4,5])

def rand7():
    choice = 0
    nested_choices = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0]
    ]
    while choice == 0:
        i = rand5() - 1
        j = rand5() - 1
        choice = nested_choices[i][j]

    return choice

print(rand7())
print(rand7())
print(rand7())
print(rand7())