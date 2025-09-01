class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # max profit
       # two pointers
       # i, j
       # iterate the prices
       #    diff between i and j ele
       #    if diff > 0
       #        update the max profit
       #    else
       #        move i to j
       #    move j by 1
        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            diff = prices[j] - prices[i]
            if diff > 0:
                max_profit = max(max_profit, diff)
            else:
                i = j

            j += 1
        return max_profit

