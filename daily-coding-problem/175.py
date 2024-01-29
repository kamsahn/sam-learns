"""
You are given a starting state start, a list of transition probabilities for a Markov chain,
and a number of steps num_steps.
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
('a', 'a', 0.9),
('a', 'b', 0.075),
('a', 'c', 0.025),
('b', 'a', 0.15),
('b', 'b', 0.8),
('b', 'c', 0.05),
('c', 'a', 0.25),
('c', 'b', 0.25),
('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

# set up distributions for each starting point
# make note of destination at each step and increment

from random import random


def run_markov(start: str, probs: list, num_steps: int) -> dict:
    prob_dict = {}
    options = list(set(p[0] for p in probs))
    
    for o in options:
        filtered_probs = [p for p in probs if p[0] == o]
        prob = 0
        prob_dict[o] = []
        for fp in filtered_probs:
            prob += fp[2]
            prob_dict[o].append((fp[1], prob))
        
    counts = dict(zip(options, [0]*len(options)))
    
    s = start
    for i in range(num_steps):
        r = random()
        starting_probs = prob_dict[s]
        
        cont = True
        i = 0
        while cont:
            p = starting_probs[i]
            if r < p[1]:
                counts[p[0]] += 1
                s = p[0]
                cont = False
            i += 1
    
    return counts
    
    
if __name__ == "__main__":
    print(run_markov("a", [
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
    ], 5000))
