"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""

# create a sublist
# order it in reverse
# replace the sublist in original list


def get_sublist(l: list, i: int, j: int) -> list:
    return l[i:j+1]


def reverse_list(l: list) -> list:
    ans = []
    for i in range(len(l)-1, -1, -1):
        ans.append(l[i])
    return ans


def reverse_sublist(l: list, i: int, j: int) -> list:
    sublist = get_sublist(l, i, j)
    reversed_sublist = reverse_list(sublist)
    before = l[0:i]
    after = l[j+1:]
    return before + reversed_sublist + after


if __name__ == "__main__":
    sample = ["s", "a", "n", "d", "w", "i", "c", "h"]
    print(reverse_sublist(sample, 1, 4))
    print(reverse_sublist(sample, 0, 4))
    print(reverse_sublist(sample, 0, 7))
    print(reverse_sublist(sample, 5, 7))



    
    