"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

# we just need to store orders to one location and we care about order
# we can use an array to accomplish this if we only care about the last element

store = []

def record(order_id):
    store.append(order_id)

def get_last(i):
    return store[-i]

record(0)
record(1)
record(2)
record(3)
record(4)

print(get_last(1))
print(get_last(5))

# for this criteria, this seems to be most efficient. If ever the user needed to access
# a specific element from the store, we might implement a dictionary for O(1) access
# get_last is O(1) access, but we have to know where the element is before we need it
