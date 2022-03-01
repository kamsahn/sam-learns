"""

Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""

def max_sub_arr(arr, k):
    start, end = 0, k
    ans = []
    while end <= len(arr):
        ans.append(max(arr[start:end]))
        start += 1
        end += 1
    return ans

# for O(n) time, O(k) space, have one sub list of k length
# remember max of that list as you shift and append the next value one at a time
# if new val is higher than old high, set as new high
# if shifted val was not high and new val is lower than old high, reuse high
# if shifted val was high, check for new high and use
# print ILO store

print(max_sub_arr([10, 5, 2, 7, 8, 7], 3))
