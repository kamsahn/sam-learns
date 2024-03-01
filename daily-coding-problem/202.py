"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""

# nope


def is_palindrome(num: int) -> bool:
    divide = []
    modulo = []
    i = 1
    while True:
        divide.append(num // i)
        modulo.append(num % i)
        print(divide)
        print(modulo)
        if i != 1 and divide[0] == modulo[-1]:
            return True
        elif divide[-1] == 0:
            return False
        i *= 10


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(888))
    print(is_palindrome(765))


