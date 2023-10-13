"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

'''
[(0, 50), (30, 75), (60, 150)]
'''

# def num_classrooms(times):
#     if len(times) == 0: return 0
#
#     num_classes = 1
#     queue = []
#     for next in times:
#         if len(queue) == 0:
#             queue.append(next)
#         else:
#             if not next[0] > any([q[1] for q in queue]):
#                 if not next[1] < any([q[0] for q in queue]):
#                     num_classes += 1
#
#     return num_classes
#
# print(num_classrooms([(30, 75), (0, 50), (60, 150), (0, 20)]))

# after learning about heaps...

from heapq import heappush, heappop

def num_classrooms(intervals):
    if not intervals: return 0
    # sort intervals by start time, end time
    sorted_intervals = sorted(intervals)
    count = 0
    heap = []

    for start, end in sorted_intervals:
        while heap and heap[0] <= start:
            heappop(heap)

        heappush(heap, end)

        count = max(len(heap), count)

    return count

print(num_classrooms([(30, 75), (0, 50), (60, 150), (0, 20), (10, 40), (40, 75)]))

