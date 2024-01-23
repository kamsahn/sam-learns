"""
Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"],
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

# iterate through s
# check for concatenated words within the current range
# add to the indices if found


def find_words(s: str, words: list[str]) -> list[int]:
    ans = []
    words_concat = "".join(words)
    length = len(words_concat)
    
    for i in range(len(s)):
        # check new substring
        temp = s[i:i+length]
        
        if len(temp) == length:
            # only check valid substrings (invalid towards the end)
            count = 0
            
            for w in words:
                if w in temp:
                    # word within substring
                    count += 1

            if count == len(words):
                # all words within substring once
                ans.append(i)
    
    return ans


if __name__ == "__main__":
    s = "dogcatcatcodecatdog"
    words = ["cat", "dog"]
    print(find_words(s, words))
    s = "barfoobazbitbyte"
    print(find_words(s, words))
    s = "catdogcatdogdogcatdogcatcat"
    print(find_words(s, words))
    s = "dogdogdogdog"
    print(find_words(s, words))
