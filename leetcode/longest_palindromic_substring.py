"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

STORE = {}

class Solution(object):
    def is_palindrome(self, sub_s):
        """
        :type sub_s: str
        :rtype: bool
        """
        start, end = 0, len(sub_s)-1
        while end >= start:
            if sub_s[start] == sub_s[end]:
                start += 1
                end -= 1
            else:
                return False
        STORE[sub_s] = True
        return True

    def pop(self, s):
        if STORE.get(s):
            return s
        return s if self.is_palindrome(s) else self.longestPalindrome(s[0:len(s)-1])

    def shift(self, s):
        if STORE.get(s):
            return s
        return s if self.is_palindrome(s) else self.longestPalindrome(s[1:len(s)])

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        from_pop = self.pop(s)
        from_shift = self.shift(s)

        return from_pop if len(from_pop) > len(from_shift) else from_shift

