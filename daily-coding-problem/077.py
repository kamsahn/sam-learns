"""
Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

# sort intervals by starting value
# for each interval, check if new end is greater than prev end
# remove intervals that are encompased
# merge intervals that overlap


def get_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    ans = []
    for interval in intervals:
        if ans:
            if ans[-1][1] < interval[1]:
                if ans[-1][1] > interval[0]:
                    # merge these two intervals
                    new_interval = (ans[-1][0], interval[1])
                    ans.pop()
                    ans.append(new_interval)
                else:
                    ans.append(interval)
        else:
            ans.append(interval)
        
    return ans


if __name__ == "__main__":
    i = [(1, 3), (5, 8), (4, 10), (20, 25)]
    print(get_intervals(i))
    i = [(1, 3), (5, 11), (4, 10), (20, 25)]
    print(get_intervals(i))
    i = [(1, 3), (5, 11), (4, 10), (20, 25), (5, 21)]
    print(get_intervals(i))
