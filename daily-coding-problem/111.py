"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

# search the string S in sections of len(W)
# check if all letters match, return index if so


def is_anagram(w: str, s: str) -> bool:
    return sorted(list(w)) == sorted(list(s))
    

def anagram_finder(w: str, s: str) -> list:
    ans = []
    w_len = len(w)
    for i in range(len(s)):
        section = s[i:i+w_len]
        if is_anagram(w, section):
            ans.append(i)
    return ans


if __name__ == "__main__":
    print(anagram_finder("ab", "abxaba"))  # expected 0, 3, 4
    print(anagram_finder("race", "racecar"))  # expected 0, 3
    print(anagram_finder("racecar", "racecar"))  # expected 0
    print(anagram_finder("r", "rrr"))  # expected 0, 1, 2
    print(anagram_finder("q", "rrr"))  # expected empty list
    print(anagram_finder("q", "rrrq"))  # expected 3



    