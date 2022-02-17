"""
Given a string, find the palindrome that can be made by inserting the fewest
number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made, return the lexicographically
earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can
add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three
letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def palindrome_finder(word):
    def is_palindrome(maybe_pal):
        max_i = len(maybe_pal) - 1
        i = 0
        is_pal = True
        while i <= max_i and is_pal:
            if maybe_pal[i] == maybe_pal[max_i]:
                i += 1
                max_i -= 1
            else:
                is_pal = False
        return is_pal

    # check if palindrome
    if is_palindrome(word):
        return word

    palindromes = []
    # check for sub palindromes (check two letters to full word)
    for i in range(0, len(word)):
        from_left = word[:i]
        from_right = word[i:]
        if len(from_left) > 1 and  is_palindrome(from_left):
            palindromes.append(word[i:][::-1] + word)
        if len(from_right) > 1 and  is_palindrome(from_right):
            palindromes.append(word + word[:i][::-1])

    if len(palindromes) > 0:
        return sorted(palindromes)[0]  # length of word?

    # add letters to beginning and end
    palindromes.append(word + word[:len(word)-1][::-1])
    palindromes.append(word[1:][::-1] + word)

    return sorted(palindromes)[0]


print(palindrome_finder('google'))
print(palindrome_finder('race'))
print(palindrome_finder('apple'))
print(palindrome_finder('gggraa'))
print(palindrome_finder('title'))


