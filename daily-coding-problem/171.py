"""
You are given a list of data entries that represent entries and exits of groups of people into a building.
An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""

# make a method that reads each data entry
# update total and keep track of max

def find_busiest(entries: list[dict]) -> tuple:
    total = 0
    busiest_count = total
    busiest_time = 0, 0
    last_ts = 0
    
    # sort by timestamp
    sorted_entries = sorted(entries, key=lambda d: d["timestamp"])
    
    for entry in sorted_entries:
        if entry["type"] == "enter":
            total += entry["count"]
        elif entry["type"] == "exit":
            total -= entry["count"]
        
        if busiest_count < total:
            busiest_count = total
            busiest_time = last_ts, entry["timestamp"]
        
        last_ts = entry["timestamp"]
    
    print("people in building:", busiest_count)
    return busiest_time

if __name__ == "__main__":
    entries = [
        {"timestamp": 1, "count": 3, "type": "enter"},
        {"timestamp": 2, "count": 2, "type": "exit"},
        {"timestamp": 3, "count": 1, "type": "exit"},
        
    ]
    print(find_busiest(entries))
    entries = [
        {"timestamp": 3, "count": 1, "type": "enter"},
        {"timestamp": 1, "count": 3, "type": "enter"},
        {"timestamp": 5, "count": 2, "type": "exit"},
        {"timestamp": 4, "count": 2, "type": "enter"},
        {"timestamp": 6, "count": 2, "type": "exit"},
        {"timestamp": 2, "count": 2, "type": "exit"},
    ]
    print(find_busiest(entries))
    
        