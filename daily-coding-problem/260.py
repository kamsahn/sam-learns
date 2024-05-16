"""
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether
each number is larger or smaller than the last.
Given this information, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""

# arrange the array in ascending order
# for every -, pop the first element (lowest element) and insert in ascending FROM THE RIGHT at all minus indices


def reconstruct_order(clue: list) -> list[int]:
    minus_indices = []
    for i in range(len(clue)):
        if clue[i] == "-":
            minus_indices.insert(0, i)
            
    ans = list(range(len(clue)))
    
    for i in minus_indices:
        temp = ans.pop(0)
        ans = ans[:i] + [temp] + ans[i:]
    
    return ans


def reconstruct_order_rev(clue: list) -> list[int]:
    high = len(clue) - 1
    low = -1
    ans = []
    for i in range(high, low, -1):
        if clue[i] == "+":
            ans.insert(0, high)
            high -= 1
        elif clue[i] == "-":
            low += 1
            ans.insert(0, low)
        else:
            low += 1
            ans.insert(0, low)
    
    return ans
            


if __name__ == "__main__":
    # print(reconstruct_order([None, "+", "+", "-", "+"]))
    # print(reconstruct_order([None, "-", "+", "-", "+"]))
    # print(reconstruct_order([None, "-", "+", "-", "+", "+", "+", "-", "-", "+"]))
    # print(reconstruct_order([None, "-", "-", "-", "-"]))
    # print(reconstruct_order([None, "+", "+", "+", "+"]))
    
    print(reconstruct_order_rev([None, "+", "+", "-", "+"]))
    print(reconstruct_order_rev([None, "-", "+", "-", "+"]))
    print(reconstruct_order_rev([None, "-", "+", "-", "+", "+", "+", "-", "-", "+"]))
    print(reconstruct_order_rev([None, "-", "-", "-", "-"]))
    print(reconstruct_order_rev([None, "+", "+", "+", "+"]))

    