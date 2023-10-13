"""
You have n fair coins and you flip them all at the same time. 
Any that come up tails you set aside. 
The ones that come up heads you flip again. 
How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""

"""
Notes:
expect half of the coins to flip to heads each time
half n each time
"""
from math import ceil, log2

def expected_flips(n):
  def expected_flips_helper(m, flips):
    flips = flips + 1
    if (m != 1):
      return expected_flips_helper(ceil(m / 2), flips)
    return flips

  return expected_flips_helper(n, 0)

print(expected_flips(100)) # 100, 50, 25, 13, 7, 4, 2, 1
print(expected_flips(1000)) # 1000, 500, 250, 125, 63, 32, 16, 8, 4, 2, 1
print(expected_flips(5)) # 5, 3, 2, 1

# allegedly the answer involves log2 and is one off from my answer
print(ceil(log2(100 + 1)))
print(ceil(log2(5 + 1)))
print(ceil(log2(2 + 1)))