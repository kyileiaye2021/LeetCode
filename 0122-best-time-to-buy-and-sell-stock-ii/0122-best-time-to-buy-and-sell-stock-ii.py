class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # twopointers
        # i and j
        # total profit
        # itereate thru the list
        #   diff 
        #   if diff > 0:
        #       add the diff to total profit
        #       move i to j
        #   else:
        #       move i to j
        #   move j by 1
        # return total profit

        i, j = 0, 1
        total_profit = 0
        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            if curr_profit > 0:
                total_profit += curr_profit

            i = j
            j += 1
        return total_profit
