"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def largest_sub_palindrome(s: str) -> str:
    largest = ""
    # count = 0  # used to justify breaks
    length = len(s)
    for i in range(length):
        temp = s[i:]
        temp_length = len(temp)
        if temp_length > len(largest):  # no need to check
            for j in range(temp_length):
                # count += 1
                sub_temp = temp[:temp_length-j]
                sub_temp_length = len(sub_temp)
                if sub_temp_length > len(largest):  # no need to check
                    if is_palindrome(sub_temp):
                        if len(largest) < sub_temp_length:
                            largest = sub_temp
                else:
                    break
        else:
            break

    # print(count)
    return largest
    

if __name__ == "__main__":
    print(largest_sub_palindrome("bananas"))
    print(largest_sub_palindrome("aabcdcb"))
    print(largest_sub_palindrome("aabcdcbbananas"))
    print(largest_sub_palindrome("aabcdcbbanananas"))
