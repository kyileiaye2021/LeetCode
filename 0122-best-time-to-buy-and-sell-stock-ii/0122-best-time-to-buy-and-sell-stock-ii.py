class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # i, j = 0 1
        # iterate thru the prices until j reaches the end
        #   profit = j ele - i ele
        #   if profit < 0:
        #       i = j 
        #       j += 1
        #   else
        #       total += proift
        #       i += 1
        #       j += 1
        # return total

        i, j = 0, 1
        total = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j

            else:
                total += profit
                i += 1

            j += 1
        return total 


        