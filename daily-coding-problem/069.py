"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

# sort numbers
# get largest three absolute values
# multiply

def largest_product(l: list[int]) -> int:
    l.sort()
    ans = l[-3]*l[-2]*l[-1]
    if l[0] < 0 and l[1] < 0:
        return max(l[0]*l[1]*l[-1], ans)
    else:
        return ans

if __name__ == "__main__":
    print("expected 500", largest_product([-10, -10, 5, 2]))
    print("expected 50", largest_product([-1, -10, 5, 2]))
    print("expected 30", largest_product([3, -10, 5, 2]))
    print("expected -100", largest_product([-10, -10, -5, -2]))
    print("expected 500", largest_product([10, -10, -5, -2]))


