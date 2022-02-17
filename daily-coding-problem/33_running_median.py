"""
Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle
 numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2
"""

def running_median(seq):
    r_seq = []
    for num in seq:
        r_seq.append(num)  # add the number to the running sequence
        r_seq.sort()  # sort the running sequence
        r_len = len(r_seq)  # get the length of the running sequence
        if r_len % 2 == 0:  # even number length, get an average
            i1, i2 = int(r_len/2), int((r_len/2)-1)
            median = (r_seq[i1] + r_seq[i2])/2
            print(median if not median.is_integer() else int(median))  # match suggested output
        else:  # odd number length, get the middle index
            print(r_seq[r_len//2])

running_median([2, 1, 5, 7, 2, 0, 5])
