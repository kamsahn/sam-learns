"""
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""


# def any_pythogorean_triplets(arr: list[int]):
#     # c = 0
#     for i in arr:
#         for j in arr:
#             if i != j:
#                 for k in arr:
#                     if i != k:
#                         # c += 1
#                         if i*i - j*j == k*k:
#                             # print(c)
#                             return j, k, i
#     # print(c)
#     return False

def any_pythogorean_triplets(arr: list[int]):
    # c = 0
    set_arr = set(arr)
    for i in arr:
        for j in arr:
            # c += 1
            if (i*i + j*j)**0.5 in set_arr:
                # print(c)
                return i, j, int((i*i + j*j)**0.5)
    # print(c)
    return False


if __name__ == "__main__":
    print(any_pythogorean_triplets([7, 13, 3, 6, 5, 1]))
    print(any_pythogorean_triplets([7, 13, 3, 6, 5, 4, 1]))
    print(any_pythogorean_triplets([6, 8, 10]))

