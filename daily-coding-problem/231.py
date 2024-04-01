"""
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""


def no_repeats(string: str) -> str:
    store = dict()
    
    for char in string:
        if char not in store:
            store[char] = 0
        store[char] += 1
    
    ans = []
    for char, count in store.items():
        if count > (len(string) / 2) + 1:
            return None
        
        if count > len(ans):
            temp = [char for _ in range(count)]
            for i in range(len(ans)):
                temp[i] += ans[i]
            ans = temp
        else:
            for i in range(count):
                ans[i] += char
    
    return "".join(ans)


if __name__ == "__main__":
    print(no_repeats("aaaabbc"))
            