"""
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import random

# generate a number between 0 and 1
# compare it to the sum of elements of probabilites
# if the current sum is greater than the random number, return corresponding number
# ex. random number 0.66
# -> 0.1 < 0.66
# -> (0.1 + 0.5) < 0.66
# -> (0.1 + 0.5 + 0.2) > 0.66
# -> third probability reached, therefore third element should be returned

def set_of_probabilities(numbers: list[int], probs: list[float]) -> int:
    r = random.random()
    prob_sum = 0
    for i in range(len(probs)):
        prob_sum += probs[i]
        if prob_sum > r:
            return numbers[i]


if __name__ == "__main__":
    store = {}
    n = 1000
    for i in range(n):
        ans = set_of_probabilities([1,2,3,4], [0.1, 0.5, 0.2, 0.2])
        
        if store.get(ans):
            store[ans] += 1
        else:
            store[ans] = 1

    print("1: ", (store[1]/n)*100, "%")
    print("2: ", (store[2]/n)*100, "%")
    print("3: ", (store[3]/n)*100, "%")
    print("4: ", (store[4]/n)*100, "%")

    