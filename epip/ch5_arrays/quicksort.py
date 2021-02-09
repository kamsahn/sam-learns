"""
quicksort was the first problem I tackled in Elements of Programming Interviews in Python (comically
abbreviated to epip). And it really kicked my butt. Having not thought about data structures or
algorithms since my interview prep days, I was really humbled. But that's in part why I wanted to start
at these challenges again.
"""

"""
Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
Hinf: Think about the partition step in quicksort
"""


def pivot_array(a, x):
    """
    A method that will loop through a list and sort it into partitions (sublists) based on its comparison to a given
    value, x. The three sublists will contain values less than, equal to and greater than the given pivot, x. The return
    value will be a list comprising of the three sublists.
    i.e.
        input:
            a = [3, 7, 8, 2, 6, 8, 1, 5, 7, 9], x = 3
        can provide a valid output:
            [2, 1, 3, 7, 8, 6, 8, 5, 7, 9]
        since the first partition
    :param a: list,
    :param x: int, index to pivot array, a, around
    :return: list, sorted into partitions based on pivot, x
    """
    # time complexity O[n]
    # space complexity O[n]
    pivot = a[x]
    less = []
    equal = []
    greater = []
    for e in a:
        if e > pivot:
            greater.append(e)
        elif e < pivot:
            less.append(e)
        else:
            equal.append(e)

    return less + equal + greater


def pivot_array_rev1(a, x):
    """
    Using some of the guidance from the book, this is my attempt to solve the problem within the original list -- using
    O(1) space complexity. It was significantly harder to wrap my head around this implementation...
    :param a: list,
    :param x: int, index to pivot array, a, around
    """
    # time complexity O[n]
    # space complexity O[1]
    pivot = a[x]
    smaller, equal, larger = 0, 0, len(a)
    while equal < larger:
        if a[equal] < pivot:
            a[equal], a[smaller] = a[smaller], a[equal]
            smaller, equal = smaller + 1, equal + 1
        elif a[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            a[equal], a[larger] = a[larger], a[equal]

    return a
