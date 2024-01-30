"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

# for each letter in word 1
# check to see if letter is in the map
# if yes, make sure that corresponds to the same index in word 2
# else add letter at index 2 to the map


def word_map(word1, word2) -> bool:
    w_map = {}
    for i in range(len(word1)):
        if word1[i] in w_map:
            if w_map[word1[i]] != word2[i]:
                return False
        else:
            w_map[word1[i]] = word2[i]
    
    return True


if __name__ == "__main__":
    print(word_map("abc", "bcd"))
    print(word_map("foo", "bar"))
    print(word_map("foo", "boo"))
    print(word_map("kotor", "levea"))
    