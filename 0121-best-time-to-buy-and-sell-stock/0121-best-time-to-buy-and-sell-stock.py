class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        # i, j 
        # max profit = 0
        # while j is < len
        #   find diff
        #   check if the diff bet i and j is <= 0
        #       move i 
        #   update max profit
        #   move j

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            cur_profit = prices[j] - prices[i]
            if cur_profit <= 0:
                i = j
            max_profit = max(cur_profit, max_profit)
            j += 1
        return max_profit

