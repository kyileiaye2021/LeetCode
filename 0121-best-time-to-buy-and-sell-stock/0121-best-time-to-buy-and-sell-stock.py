class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        #Hashmap Approach
        #create a hashmap {val: profit}
        #iterate over the price
        #max value from i+1 to len of the list
        #subtract the current val from max value which is the profit
        #store the profit in the map

        #max_profit = 0
        #after the loop, iterate over the hashmap to find the largest profit
        #return the max_profit

        hash_map = {}
        for i, n in enumerate(prices):
            price_sublst = prices[i:len(prices)]
            max_value = max(price_sublst)
            profit = max_value - n
            if profit <= 0:
                hash_map[n] = 0
            else:
                hash_map[n] = profit
    
        max_profit = 0
        for profit in hash_map.values():
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
        '''
        
        #Two pointer approach
        #create two vars (l, r) represeenting index 0 and 1
        #create a var max_profit to keep track of the max profit
        #iterate over the lst
        #if lst[r] > lst[l]:
        #find the profit and update the max
        #if not, l = r

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1

        return max_profit
        