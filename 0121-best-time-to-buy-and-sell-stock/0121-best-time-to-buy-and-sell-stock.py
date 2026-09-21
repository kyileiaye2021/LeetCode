class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # prices = [7, 1,2,5]
        # profit = 4

        # prices = [1,6,3,2]
        # profit = 5

        # prices = [5,3,1]
        # profit = 0

        # prices = [4,4,4]
        # profit = 0

        # prices = [3]
        # profit = 0

        # 2 pointers

        # i, j 

        max_profit = 0
        i = 0
        j = 1

        while j < len(prices):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

            if profit < 0:
                i = j
        
            j += 1
        return max_profit






        