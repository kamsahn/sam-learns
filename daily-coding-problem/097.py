"""
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time,
it will maintain that value forever or until it gets set at a later time.
In other words, when we get a key at a time,
it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""

# create a class that holds time as well as key/value
# get methods should access the value at closet time >= given t
# time can be arranged in an ordered list
# sample format:

"""
timeline = {
    0: {
        key1: value1,
        key2: value2,
        ...
    },
    2: {
        key1: value1,
        key3: value3
    },
    ...
}
"""

class TimeMap:
    def __init__(self):
        self.timeline = {}
    
    def set_with_t(self, key: any, value: any, time: int):
        if self.timeline.get(time, None):
            self.timeline[time][key] = value
        else:
            self.timeline[time] = {key: value}
    
    def get_with_t(self, key: any, time: int):
        temp = None
        latest = -1
        for t in self.timeline.keys():
            if self.timeline[t].get(key, None):
                if latest < t <= time:
                    temp = self.timeline[t][key]
                    latest = t
        
        print(temp)  # or return and print later
        

if __name__ == "__main__":
    tm = TimeMap()
    tm.set_with_t(1, 1, 0)
    tm.set_with_t(2, "a", 0)
    tm.set_with_t(2, "b", 1)
    tm.set_with_t(2, "c", 5)

    tm.get_with_t(1, 1)
    tm.get_with_t(2, 0)
    tm.get_with_t(2, 3)
    tm.get_with_t(2, 10)
    
    d = TimeMap()
    d.set_with_t(1, 1, 0) # set key 1 to value 1 at time 0
    d.set_with_t(1, 2, 2) # set key 1 to value 2 at time 2
    d.get_with_t(1, 1) # get key 1 at time 1 should be 1
    d.get_with_t(1, 3) # get key 1 at time 3 should be 2
    
    d = TimeMap()
    d.set_with_t(1, 1, 5) # set key 1 to value 1 at time 5
    d.get_with_t(1, 0) # get key 1 at time 0 should be null
    d.get_with_t(1, 10) # get key 1 at time 10 should be 1
    
    d = TimeMap()
    d.set_with_t(1, 1, 0) # set key 1 to value 1 at time 0
    d.set_with_t(1, 2, 0) # set key 1 to value 2 at time 0
    d.get_with_t(1, 0) # get key 1 at time 0 should be 2
