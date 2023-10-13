"""
Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary. If no such itinerary exists, return null. If there are multiple
possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'),
('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return
the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport
'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even
though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first
one is lexicographically smaller.
"""

def flight_itinerary(starting_point, flights):
    def check_for_start(_starting_point):
        for f in flights:
            if f[0] == _starting_point:
                return f
        return False

    flights.sort()  # return shortest result, lexicographically
    itinerary = [starting_point]
    while flights:
        next_flight = check_for_start(itinerary[-1])
        if next_flight:
            itinerary.append(next_flight[1])
            flights.remove(next_flight)
        else:
            break
    return False if len(itinerary) < 3 else itinerary

print(flight_itinerary('YUL', [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]))
print(flight_itinerary('COM', [('SFO', 'COM'), ('COM', 'YYZ')]))
print(flight_itinerary('A', [('A', 'C'), ('B', 'C'), ('C', 'A'), ('A', 'B')]))
