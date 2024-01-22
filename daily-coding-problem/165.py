"""
Given an array of integers,
return a new array where each element in the new array is the number of smaller elements
to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

# first attempt
# for each element, count the number of smaller numbers
# create new list with count

def smaller_numbers_list(original: list[int]) -> list[int]:
    ans = []
    for i in range(len(original)):
        count = 0
        for j in range(i+1, len(original)):
            if original[i] > original[j]:
                count += 1
        ans.append(count)
    return ans

if __name__ == "__main__":
    print(smaller_numbers_list([3, 4, 9, 6, 1]))
            
            
        