"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def longest_substring(s, k):
    """
    :param s: str, string of characters
    :param k: int, number of desired unique characters in substring
    """
    outer_store = []  # holds sub strings
    def check_k(sub_s, k):
        print(sub_s)
        """check if there are k or less unique characters in sub_s"""
        store = {}  # holds character and their counts
        for char in sub_s:
            if not store.get(char):
                store[char] = 0
            store[char] += 1

        # count unique characters
        count = 0
        for char in store:
            if store[char] == 1:
                count += 1

        return True if count <= k else False

    lds = ''  # longest distinct substring
    for char in s:
        lds += char
        is_valid = check_k(lds, k)
        if not is_valid:
            # add valid string to outer store
            outer_store.append(lds[:-1])
            # remove first value of string and continue
            lds = lds[1:]

    # whole string is valid
    max_length = 0
    res = ''
    print(outer_store)
    for sub_s in outer_store:
        if len(sub_s) > max_length:
            max_length = len(sub_s)
            res = sub_s

    return res


print(longest_substring('abcba', 2))
