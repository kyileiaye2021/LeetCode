class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # happy cases
        # input - [1,2,3,4]
        # output - 3
        
        # input - [7,3,5,1,6]
        # output - 5
        
        # input - [3,1,2,5]
        # output - 4
        
        # edge cases
        # input - [4,3,2,1]
        # output - 0
        
        # input - [3,3,3]
        # output - 0
        
        # Brute force approach (O(n^2))
        # Two pointer approach (O(n))
        
        # low level steps
        # initialize two pointers 
        # i will point to second ele in nums
        # j will point to first ele in nums
        # One pointer i will iterate over the list
        # Another pointer j will be pointing to the current smallest num in the list
        # while i is less than the length of the lst
        #   check if the curr j ele is not less than i ele
        #       point j to i
        #   increment i
        
        i, j = 1, 0
        max_profit = 0
        
        while i < len(prices):
            if prices[j] >= prices[i]:
                j = i
               
            else:
                profit = prices[i] - prices[j]
                max_profit = max(max_profit,profit)
                
            i += 1
                
        return max_profit
            
                
        
        