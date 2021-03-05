"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""

# must look through every element as least once O(n)
# every other element can be subtracted from the whole sum? at alternating indecies?
# if elements are positive, answer should be using at least half of the elements
# keep track of 4 elements at a time to account for the following:
    # start + (start+2)
    # start + (start+3)
    # (start+1) + (start+3)
# can it be recursive? send a chain to the back and return with a bunch of comparisons?

# def largest_non_adjacent_sum(l):
#     sum = 0
#     i0, i1, i2, i3 = 0, 1, 2, 3
#     while i2 < len(l):
#         # options
#         first = l[i0] + l[i2]
#         second = l[i0] + l[i3] if i3 < len(l) else None
#         third = l[i1] + l[i3] if i3 < len(l) else None
#
#         options = [o for o in [first, second, third] if o is not None]
#         max_option = max(options)
#
#         sum += max_option
#         if max_option == first:
#             # next option starts at i2
#             i0 += 2
#             i1 += 2
#             i2 += 2
#             i3 += 2
#         else:
#             # next option starts at i3
#             i0 += 3
#             i1 += 3
#             i2 += 3
#             i3 += 3
#         print(i0, i1, i2, i3)
#         print(max_option)
#
#     return sum

# def largest_non_adjacent_sum(l):
#     sum = 0
#     start = 0
#     while start+1 <= len(l):
#         first = sum + l[start]
#         second = sum + l[start+1]
#         max_option = max([first, second])
#         sum = max_option
#         if max_option == first:
#             start += 2
#         else:
#             start += 3
#     return sum

def largest_non_adjacent_sum(l):
    sum = 0
    start = 0
    while start+2 < len(l):
        print(start)
        first = l[start] + l[start+2]
        second = l[start+1] + (l[start+3] if start+3 < len(l) else 0)
        third = l[start] + (l[start+3] if start+3 < len(l) else 0)

        max_option = max([first, second, third])
        sum += max_option

        if max_option == first:
            if start != 0:
                sum -= l[start]
            start += 2

        elif max_option == second:
            if start != 0:
                sum -= l[start+1]
            start += 3

        elif max_option == third:
            if start != 0:
                sum -= l[start]
            start += 3

        print(sum)
        print('---')


    return sum


# print(largest_non_adjacent_sum([2, 4, 6, 2, 5]))  # 13
# print(largest_non_adjacent_sum([5, 1, 1, 5]))  # 10
print(largest_non_adjacent_sum([6, 8, 3, 5, 7, 9, 0, 2, 4, 6]))  # 30


