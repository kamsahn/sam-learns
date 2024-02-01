"""
Given a array of numbers representing the stock prices of a company in chronological
order, write a function that calculates the maximum profit you could have made from
buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the
stock at 5 dollars and sell it at 10 dollars.
"""


def get_max_profit(prices: list) -> int:
    if len(prices) < 2:  # out of range protection
        return None
    
    min_price = prices[0]
    max_profit = max(0, prices[1] - prices[0])
    
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit


if __name__ == "__main__":
    print(get_max_profit([9, 11, 8, 5, 7, 10]))
    print(get_max_profit([1, 2, 3, 4]))
    print(get_max_profit([4, 3, 2, 1]))
    print(get_max_profit([9]))
    print(get_max_profit([9, 10]))
    print(get_max_profit([9, 11, 8, 5, 7, 10, 11, 12, 7]))
