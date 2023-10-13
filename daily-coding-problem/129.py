"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

"""
exhaustively try whole numbers until we find or exceed n... 
"""

def find_square_root(n: int) -> int:
  i = 1
  while ((i**2) <= n):
    if (i**2) == n:
      return i
    i = i + 1
  return None

print(find_square_root(9))
print(find_square_root(10))
print(find_square_root(100))
print(find_square_root(10000))
print(find_square_root(342523456234))

# binary search for floats