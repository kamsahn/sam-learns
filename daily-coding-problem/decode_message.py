"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

encoding = {
    "1": "a","2": "b","3": "c","4": "d","5": "e","6": "f","7": "g","8": "h","9": "i","10": "j","11": "k","12": "l","13": "m",
    "14": "n","15": "o","16": "p","17": "q","18": "r","19": "s","20": "t","21": "u","22": "v","23": "w","24": "x","25": "y","26": "z"
}

def decode(s):
    # "assume that the messages are decodable"
    count = 1
    # edge case
    if len(s) == 1: return count

    # look for 0's 1's and 2's
    for i in range(len(s)):
        if s[i] in ["1", "2"]:
            if (i > 0 and s[i-1] != "0") or i == 0:
                if i+2 <= len(s) and encoding.get(s[i:i+2]):
                    count += 1

    return count



    # # check every 2 to see if between 10 and 26
    # first, second = 0, 2
    # while len(s) >= second:
    #     sub_m = s[first:second]
    #     if encoding.get(sub_m):
    #         first += 2
    #         second += 2
    #     else:
    #         first += 1
    #         second += 1

print(decode('1111'))
# 1 1 1 1
# 11 11
# 11 1 1
# 1 1 11
# 1 11 1
