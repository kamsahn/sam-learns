"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true.
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""

'''
construct re into an interable
know what to do with asterisk "chains" (need to match anything or need to match a specific character)
'''

def myregex(re, input):
    starts_with_special = False
    ends_with_special = False
    if re.startswith('.') or re.startswith('*'):
        starts_with_special = True
    if re.endswith('.') or re.endswith('*'):
        ends_with_special = True

    if starts_with_special:
        pass  # to implement
    else:
        if ends_with_special:
            for i in range(len(re)):
                if re[i]
                if re[i] != input[i]:
                    return False


    # for i in range(len(re)):
    #     if re[i] == '.':
    #         pass  # do for single element
    #     elif re[i] == '*':
    #         pass # do for multiple element?

print(myregex('ra.', 'ray'))
