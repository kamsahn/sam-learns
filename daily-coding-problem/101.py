"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""


def is_prime(n):
    if n > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(n/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def goldbach(n: int) -> tuple:
    for i in range(n):
        if is_prime(i):
            temp = n - i
            if is_prime(temp):
                return i, temp
    return ()
            

if __name__ == "__main__":
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(7))  # works for some odd numbers
    print(goldbach(11))
    print(goldbach(10))
    print(goldbach(100))
