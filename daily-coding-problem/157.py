"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
"""

# count instances of each letter
# if all instances are even or all but one, return true
# else false


def any_palindrome(word: str) -> bool:
    store = {}
    for letter in word:
        if letter in store:
            store[letter] += 1
        else:
            store[letter] = 1
    
    odd_count = 0
    for letter in store:
        if store[letter] % 2 != 0:
            odd_count += 1
    
    return odd_count == 0 or odd_count == 1


if __name__ == "__main__":
    print(any_palindrome("carrace"))
    print(any_palindrome("daily"))
    print(any_palindrome("aabbccss"))
    print(any_palindrome("aabbccsss"))
    print(any_palindrome("aabbcs"))

        