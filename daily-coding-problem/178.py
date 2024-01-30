"""
Alice wants to join her school's Probability Student Club.
Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six.
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""

# doesn't matter

import random


def roll_die() -> int:
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_five_six(count: int = 0) -> int:
    roll1 = roll_die()
    count += 1
    if roll1 == 5:
        count += 1
        roll2 = roll_die()
        if roll2 == 6:
            return count
    return roll_five_six(count)


def roll_five_five(count: int = 0) -> int:
    roll1 = roll_die()
    count += 1
    if roll1 == 5:
        count += 1
        roll2 = roll_die()
        if roll2 == 5:
            return count
    return roll_five_six(count)
    
    
if __name__ == "__main__":
    n = 1000
    ff = []
    fs = []
    for i in range(n):
        rollff = roll_five_five()
        ff.append(rollff)
        rollfs = roll_five_six()
        fs.append(rollfs)

    print(f"Average cost to roll a 5 then a 5: ${(sum(ff) / n):.2f}")
    print(f"Average cost to roll a 5 then a 6: ${(sum(fs) / n):.2f}")
        
        
    
