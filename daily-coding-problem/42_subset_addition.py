"""
Given a list of integers S and a target number k, write a function that returns
a subset of S that adds up to k. If such a subset cannot be made, then return
null.

Integers can appear more than once in the list. You may assume all numbers in
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
since it sums up to 24.
"""

def subset_addition(integers, target):
    possible_ans = []
    for i in integers:
        if i == target:
            return [i]
        elif i < target:
            for pa in possible_ans:
                new_sum = sum(pa) + i
                if target - new_sum == 0:
                    return pa + [i]
                elif target - new_sum > 0:
                    pa.append(i)
            possible_ans.append([i])

    print
    return None




s = [12, 1, 61, 5, 9, 2]
k = 24

print(subset_addition(s, k))