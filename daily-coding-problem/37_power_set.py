"""
The power set of a set is the set of all its subsets. Write a function that,
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

# frozenset is a builtin that indicates we won't alter the set

def power_set(original_set):
    def power_set_helper(curr_set, power_set):
        power_set.add(frozenset(curr_set))
        for i in curr_set:
            copy_set = curr_set.copy()
            copy_set.remove(i)
            power_set.add(frozenset(copy_set))
            power_set = power_set_helper(copy_set, power_set)
        return power_set

    power_set = power_set_helper(original_set, set())
    return [set(i) for i in power_set]


print(power_set({1, 2, 3}))
print(power_set({0, 1, 2, 3, 5}))