# 5/21/19

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    lowest = float("inf")
    second_lowest = float("inf")
    for num in numbers:
        if num < lowest:
            lowest = num
        elif num < second_lowest:
            second_lowest = num
    return lowest + second_lowest
