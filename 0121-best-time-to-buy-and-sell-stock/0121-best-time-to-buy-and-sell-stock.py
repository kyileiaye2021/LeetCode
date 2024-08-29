class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # happy cases 
        # input - [7,1,5,3,6,4]
        # output - 5
        
        # edge cases
        # input - [7,6,4,3,1]
        # output - 0
        
        # input - [2,2,2,2,2]
        # output - 0
        
        # Two pointer approach
        # create a var max_profit to trace the max difference between prices
        # low and high pointing to 0 and 1
        # go over the list until high passes the length of the list
        #   check if the right pointer ele is greater than left pointer ele
        #       find the difference of the two pointer ele 
        #       update the max_profit if difference is greater than curr max_profit
        #       increment right pointer by 1
        #   assign left pointer to right 
        #   increment right pointer by 1
        
        max_profit = 0
        low, high = 0, 1
        
        while high < len(prices):
            if prices[high] > prices[low]:
                difference = prices[high] - prices[low]
                max_profit = max(max_profit, difference)
                
            else:
                low = high
                
            high += 1
            
        return max_profit
                