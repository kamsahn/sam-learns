"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35},
it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

# sum the whole set -> divide by 2 -> check if numbers can add up to that
# to check, order the set, descending order
# at each step, check to see if 

def same_subset_sums(l: list[int]) -> bool:
    if sum(l) % 2 != 0:
        return False
    

3, 1, 4, 2, 7, 3, 2 