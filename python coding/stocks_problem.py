"""
You’re given an array prices where prices[i] is the price of a stock on day i.
You can make as many transactions as you want. A transaction = buy 1 share on some day then sell it later on another day. But you must sell before you buy again (so you can hold at most one share at a time).
Goal: maximize total profit.

Important constraints (this version):

unlimited transactions allowed,

no transaction fee,

no cooldown days,

must sell before next buy.
"""

"""
You are given an  prices where prices represents the price of a stock on day .

You may complete as many transactions as you want

(buy one day → sell another day),

but you must sell the stock before buying again.

prices = [7, 1, 5, 3, 6, 4]

o/p 7

"""


def get_profit(prices: list):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]
    return profit


def get_profit_dp(prices: list):
    profit = 0
    i = 0
    n = len(prices)
    if n <= 0:
        return 0
    while i < n - 1:
        # find best price[i] to buy i.e., price[i]<price[i+1]
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        buy_price = prices[i]

        # find best price[i] to sale i.e., price[i]>price[i+1]
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        sale_price = prices[i]

        profit += sale_price - buy_price

    return profit


pr = get_profit([7, 1, 5, 6, 8, 4])
pr_1 = get_profit_dp([7, 1, 5, 6, 8, 4])
print(pr, pr_1)




