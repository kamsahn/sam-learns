"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def first_recurring(s: str):
    store = {}
    for i in s:
        if store.get(i):
            return i
        else:
            store[i] = 1
    return None

if __name__ == "__main__":
    print(first_recurring("acbbac"))
    print(first_recurring("abcdef"))
    print(first_recurring("abcdeff"))