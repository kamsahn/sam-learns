"""
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, 
return the maximum profit you can make from k buys and sells. 
You must buy the stock before you can sell it, 
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""

"""
First thoughts:
you must step through the entire list to see all your options at least once
keep track of highest k differences of n(k) - n(k-1)
return sum of differences

realizing the solution will be wrong, since I don't account for saving to sell at highest margin,
I will solve for the case where you always sell the next day
"""

profits = []

# sort difference list in place
def sort_list():
  profits.sort()

def list_full(k: int) -> bool:
  return len(profits) > k

# compare to current highs and add / replace if necessary
# save as new high
# bump a high if necessary
def compare(k: int, new: int):
  lowest = profits[0] if len(profits) else 0
  if ((new > lowest or not list_full(k)) and new > 0):
    # profit is positive
    # and (new profit is larger than a profit we've seen
    # or profit list is not full)
    profits.append(new)
    if (list_full(k)):
      # need to drop a profit
      profits.pop(0)
    sort_list()

# check difference of two places
def get_difference(n1: int, n2: int) -> int:
  return n2 - n1

# traverse the list
def traverse(k: int, prices: list) -> int:
  for idx, _ in enumerate(prices):
    # stop before we hit the end of the list
    if (len(prices) - 1 > idx):
      compare(k, get_difference(prices[idx], prices[idx+1]))
  return sum(profits)

print(traverse(2, [5, 2, 4, 0, 1]))
