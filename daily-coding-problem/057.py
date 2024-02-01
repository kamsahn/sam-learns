"""
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""

def get_line_breaks(s: str, k: int) -> list:
    ans = []
    temp_s = ""
    
    for i in range(len(s)):
        if len(temp_s) == k:
            if s[i] == " ":
                # next char is a space -> append the temp string
                ans.append(temp_s)
                temp_s = ""
            else:
                # word is continuing -> break at beginning of word
                if " " not in temp_s:
                    return None  # cannot break up these lines
                
                for j in range(1, k):
                    ii = k - j
                    if temp_s[ii] == " ":
                        ans.append(temp_s[:ii])
                        break  # don't find more spaces
    
                temp_s = temp_s[ii+1:]

        temp_s += s[i]
        if temp_s == " ":  # catch starting spaces
            temp_s = ""
    
    ans.append(temp_s)  # append remaining
    return ans


if __name__ == "__main__":
    print(get_line_breaks("the quick brown fox jumps over the lazy dog", 10))
    print(get_line_breaks("the quick brownfoxjumpsoverthelazydog", 10))
    print(get_line_breaks("the quick brown fox jumps over the lazy dog", 9))
    print(get_line_breaks("the quick brown fox jumps over the lazy dog", 15))
    print(get_line_breaks("the quick brown fox jumps over the lazy dog", 20))
    print(get_line_breaks("the quick brown fox jumps over the lazy dog", 3))

                    
                