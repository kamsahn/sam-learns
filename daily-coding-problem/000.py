"""
that one question where you need to find total profit from a list of prices

ex: prices: [4, 5, 6, 5, 2, 5] -> returns 3 since you can buy at 2 an sell at 5
"""


def highest_profit(prices: list[int]) -> int:
    p = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            p = max(p, prices[j] - prices[i])
            print(i, j, p)
    return p


def highest_profit2(prices: list[int],
                    profit: int = 0,
                    lowest: int = 0) -> int:
    for i in range(len(prices)):
        lowest = min(lowest, i)
        profit = max(profit, i+1 - lowest)
        return max(profit, highest_profit2(prices, profit, lowest))


if __name__ == "__main__":
    print(highest_profit([4, 5, 6, 5, 2, 5]))
    print(highest_profit2([4, 5, 6, 5, 2, 5]))
