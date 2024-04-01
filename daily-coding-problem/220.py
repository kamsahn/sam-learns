"""
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game.
You and an opponent take turns choosing either the first or last coin from the row, removing it from the row,
and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty,
if you move first, assuming your opponent plays optimally.
"""

def max_earnings(coins: list[int]) -> int:
    earnings = 0
    turn = 1  # your turn is on odd numbers
    while len(coins) > 0:
        # identify the maximum value coin
        max_val = max(coins[0], coins[-1])
        # remove it from the row
        if coins[0] > coins[-1]:
            coins = coins[1:]
        else:
            coins = coins[:-1]
        # add it to your earnings if its your turn
        if turn % 2 != 0:
            earnings += max_val
        # pass the turn to next player
        turn += 1
    
    return earnings


if __name__ == "__main__":
    coins = [1, 5, 25, 25, 1, 1, 10, 5]
    print("expected: 36, actual:", max_earnings(coins))
    coins = [1, 5, 25, 25, 1, 1, 10, 5, 1, 25, 1, 1, 50, 25, 5, 10]
    print("expected: 97, actual:", max_earnings(coins))