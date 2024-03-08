"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

# iterate once,
# for every time you find an occurance of the starting letter
# create a new entry
# if the entry is eventually completed, add that starting index to the answer


def get_starting_indices(string: str, pattern: str) -> list[int]:
    ans = []
    instances = {}
    start = pattern[0]
    
    for i in range(len(string)):
        char = string[i]
        
        remove = []
        for k, v in instances.items():
            v += char
            instances[k] = v
            if v == pattern:
                ans.append(k)
                remove.append(k)
            elif v != pattern[:len(v)]:
                remove.append(k)
        
        for j in remove:
            del instances[j]
        
        if start == char:
            instances[i] = char

    return ans


if __name__ == "__main__":
    print(get_starting_indices("abracadabra", "abr"))
    print(get_starting_indices("abczzzabczzaabcab", "abc"))
    print(get_starting_indices("aaaa", "aa"))
    print(get_starting_indices("abaaa", "aa"))
