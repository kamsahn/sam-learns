"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5,
since the longest common subsequence is "eieio".
"""

# find a common subset by:
# split the letters into a list
# filter each list by only common letters

# for each letter in one subset
# if the other subsets have it after the latest i, add it to the longest holder


def get_common_letters(s1, s2, s3):
    l1, l2, l3 = list(s1), list(s2), list(s3)
    l1_common = [e for e in l1 if e in l2 and e in l3]
    l2_common = [e for e in l2 if e in l1 and e in l3]
    l3_common = [e for e in l3 if e in l1 and e in l2]
    return l1_common, l2_common, l3_common


def get_longest_substring(l1, l2, l3):
    longest = ""
    last_i_2 = -1
    last_i_3 = -1
    for i in range(len(l1)):
        letter = l1[i]
        temp = longest + letter
        
        letter_i_in_l2 = [j for j in range(len(l2)) if l2[j] == letter and j > last_i_2]
        letter_i_in_l3 = [j for j in range(len(l3)) if l3[j] == letter and j > last_i_3]
        
        if len(letter_i_in_l2) and len(letter_i_in_l3):
            last_i_2 = letter_i_in_l2[0]
            last_i_3 = letter_i_in_l3[0]
            longest = temp
    
    return longest


def main(s1, s2, s3):
    l1, l2, l3 = get_common_letters(s1, s2, s3)
    return get_longest_substring(l1, l2, l3)


if __name__ == "__main__":
    print(get_longest_substring("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"))
    print(get_longest_substring("abzzzcde", "abyyycde", "abxxxcde"))
    print(get_longest_substring("abzzzcde", "yyycde", "abxxxcde"))


    