class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i =0
        j = 1
        total = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit > 0:
                total += profit
            
            i = j
            j += 1

        return total
                    


            
        