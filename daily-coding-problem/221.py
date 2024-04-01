"""
Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7.
The first few sevenish numbers are 1, 7, 8, 49, and so on.
Create an algorithm to find the nth sevenish number.
"""


def nth_sevenish(n: int) -> int:
    nums = []
    powers = []
    power = 0

    while len(nums) < n:
        temp = 7**power
        nums.append(temp)
        for p in powers:
            nums.append(temp + p)

        powers.append(temp)
        power += 1
        print(nums)
        print(powers)
    
    return nums[n-1]


if __name__ == "__main__":
    print(nth_sevenish(1))
    print(nth_sevenish(2))
    print(nth_sevenish(3))
    print(nth_sevenish(4))
    print(nth_sevenish(5))
    print(nth_sevenish(6))
    print(nth_sevenish(7))
    