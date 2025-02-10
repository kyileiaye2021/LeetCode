class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if current jth ele is > than the ith ele
        #   move i to j and j by 1
        # else:
        #   calculate profiit and keep track of the max profit

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            
            else:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                
            j += 1

        return max_profit