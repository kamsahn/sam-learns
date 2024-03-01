"""
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578
"""

# ye olde find the first number to break true descending (from right to left)
# replace the largest place with the smallest int that is greater than the previous place
# arange the remaining numbers in ascending order (from right to left)
"""
i.e. given 48975, check numbers from the right
5
7
9
8 -> this is the first number that breaks the right-to-left ascending pattern
9 => min([i for i in [5, 7, 9] if i > 8]) so we replace 9 as the "leading" place
then arrange the rest of the numbers in left-to-right ascending -> 9578
"""

def next_permutation(num: int) -> int:
    str_num = str(num)
    last_num = int(str_num[-1])
    r2l = [last_num]
    
    for i in range(1, len(str_num)):
        r2l.append(int(str_num[-i - 1]))
        if r2l[-1] < r2l[-2]:  # right to left ascending has ended
            # remove the last element and save as highest place int
            highest_place = r2l[-1]
            r2l.pop()
            # find the smallest int that is greater than the highest place int
            replacement = min([i for i in r2l if i > highest_place])
            # "swap" the replacement and highest place
            r2l.remove(replacement)
            r2l.append(highest_place)
            # arange the trailing numbers in ascending order
            r2l.sort()
            # get the remaining number
            remaining = str_num[:-i - 1]
            # line them all up in a string and convert them back to an int
            return int(remaining + str(replacement) + "".join([str(i) for i in r2l]))

    # there is no next permutation in absolute order
    # could also return None
    return num


if __name__ == "__main__":
    print("48975 ->", next_permutation(48975))
    print("5793 ->", next_permutation(5793))
    print("1234 ->", next_permutation(1234))
    print("4321 ->", next_permutation(4321))

