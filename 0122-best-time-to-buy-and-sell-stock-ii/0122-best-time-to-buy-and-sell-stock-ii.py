class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, j
        # total profit
        # max profit
        # iterate thru the list until j reaches the end
        #   find the cur profit
        #   if cur profit > max profit
        #       update the max profit
        #       move j pointer
        #   else:
        #       update total
        #       move i to j pointer
        #       reset max profit to 0
        #       move j pointer

        i, j = 0, 1
        total = 0

        while j < len(prices):
            # if we can make profit
            #   sell the stock, make profit, and rebuy at the same day
            # else:
            #   buy the product

            profit = prices[j] - prices[i]
            if profit > 0:
                total += profit
            i = j # rebuy immediately after selling at the same day
            j += 1
                  
        return total
