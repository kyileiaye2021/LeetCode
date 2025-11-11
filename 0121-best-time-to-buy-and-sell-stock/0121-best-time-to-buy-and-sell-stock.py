class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = float('inf')

        for i in range(len(prices)):
            if cheapest != float('inf'):
                profit = max(profit, prices[i] - cheapest)
        
            cheapest = min(prices[i], cheapest)

        return profit

       # store the max profit for each day so far

       # profit = 0
       # cheapest price = inf
       # temp list to store the max profit for each day

       # iterate thru the list
       #    profit[i] = ith price - cheapest price
       #    update cheapest price with the curr price if curr price is smaller
       # iterate thru temp list and return the max profit





