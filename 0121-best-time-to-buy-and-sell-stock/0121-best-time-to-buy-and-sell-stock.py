class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # i, j - 0, 1
        # iterate thru the arr until j reaches the end
        #   if j ele < i ele
        #       move i to j
        #       move j by 1
        #   else
        #       curr profit = j ele - i ele
        #       update max profit if curr profit > max profit
        # return max profit

        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            if prices[j] <= prices[i]:
                i = j

            else:
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)

            j += 1

        return max_profit

                


        