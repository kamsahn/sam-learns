"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

# sort the intervals
# for each, check if the end is higher than the next start
# if so, remove (add to remove count)
# else, add to answer


def min_intervals_removed(intervals: list[tuple]) -> int:
    removed = 0
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            removed += 1
    return removed


if __name__ == "__main__":
    intervals = [(7, 9), (2, 4), (5, 8)]
    print(min_intervals_removed(intervals))
    intervals = [(7, 9), (2, 4), (5, 8), (2, 3)]
    print(min_intervals_removed(intervals))
    intervals = [(1, 10), (2, 3), (3, 4), (4, 5), (10, 11)]
    print(min_intervals_removed(intervals))
