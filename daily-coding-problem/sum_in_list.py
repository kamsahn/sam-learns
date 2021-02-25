"""
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def sum_in_list(l, k):
    store = {}
    for num in l:
        comp = k - num
        if store.get(comp, None) is not None:
            return True
        store[num] = num
    return False


print(f'l=[10,15,3,7], k=17 -> {sum_in_list([10,15,3,7], 17)}')
print(f'l=[10,15,3,7], k=22 -> {sum_in_list([10,15,3,7], 22)}')
print(f'l=[], k=22 -> {sum_in_list([], 22)}')
print(f'l=range(1000), k=1999 -> {sum_in_list(range(1000), 1999)}')
print(f'l=range(1001), k=1999 -> {sum_in_list(range(1001), 1999)}')
