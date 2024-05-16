"""
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k,
write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return False.
"""


def string_matcher(n: str, k: str) -> int:
    for i in range(len(n)):
        if n[i:i+len(k)] == k:
            return i
    return False


if __name__ == "__main__":
    print(string_matcher("abcdefg", "cde"))
    print(string_matcher("abcdefg", "efg"))
    print(string_matcher("abcdefg", "g"))


    