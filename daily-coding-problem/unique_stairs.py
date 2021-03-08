"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# It happens that with the options of 1 and 2 steps at a time,
# N and number of unique ways correspond to the index and value of the fibonacci sequence

# 0 stairs -> 0 ways
# 1 stair -> 1 way
# 2 stairs -> 2 ways
# 3 stairs -> 3 ways
# 4 stairs -> 5 ways
# 5 stairs -> 8 ways
# 6 stairs -> 13 ways

# that being said, we might be able to use a similar approach to implementing a
# fibonacci method with memoization

# compute the number of unique ways for range(1, N+1) and save unique ways as you go
def unique_stairs(N):
    step = 1
    store = {}
    def unique_stairs_helper(store, step):
        # check if there was a previous step
        if store.get(step-1):
            old_unique_ways = store[step-1]
        else:
            old_unique_ways = [[]]

        # add another step to the unique ways list
        print(old_unique_ways)
        new_unique_ways = []
        for uw in old_unique_ways:
            new_unique_ways.append(uw.append(1))
        for uw in old_unique_ways:
            if [1] + uw not in new_unique_ways:
                new_unique_ways.append([1] + uw)

        store[step] = new_unique_ways

        return unique_stairs_helper(store, step+1)

    while step <= N:
        unique_stairs_helper(store, step)

    return len(store[step])

print(unique_stairs(4))
