"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_distance(str_one, str_two):
    def directional_distance(_str_one, _str_two):
        more = True
        i = 0
        distance = 0
        while more:
            try:
                if not _str_one[i] == _str_two[i]:
                    distance += 1
                i += 1
            except IndexError:
                distance += abs(len(_str_one) - len(_str_two))
                more = False
        return distance
    left_distance = directional_distance(str_one, str_two)
    right_distance = directional_distance(str_one[::-1], str_two[::-1]) # reveresed

    return min(left_distance, right_distance)

# ultimate method would be compare two strings from one end to another, find the
# lowest difference and use that

def edit_distance_wip(str_one, str_two):
    def directional_distance(_str_one, _str_two):
        more = True
        i = 0
        distance = 0
        while more:
            try:
                if not _str_one[i] == _str_two[i]:
                    distance += 1
                i += 1
            except IndexError:
                distance += abs(len(_str_one) - len(_str_two))
                more = False
        return distance

    min_distance = 1000
    # need to do the same for string two?
    # need to make sure str_one is shorter?
    for i in range(len(str_one)):
        curr_distance_one = directional_distance(str_one[i:len(str_one)], str_two)
        curr_distance_two = directional_distance(str_one[0:i], str_two)
        min_distance = min(min_distance, curr_distance_one)
        min_distance = min(min_distance, curr_distance_two)

    return min_distance



print(edit_distance('kitten', 'sitting'))
print(edit_distance('swim', 'swarm'))
print(edit_distance('apple', 'a'))
print(edit_distance('battle', 'attle'))
print(edit_distance('vapplev', 'apple'))
print(edit_distance('abcz', 'zdef'))