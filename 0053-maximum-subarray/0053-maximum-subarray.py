class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Happy cases
        # input - nums = [-2,1,2]
        # output - 3
        
        # Edge cases
        # input - nums = [-1,1]
        # output - 1
        # input - nums = [2]
        # output - 2
        
        # Brute Force approach (O(n^2))
        # Sliding Window approach (O(n))
        
        # create a max sub_total to trace the max sub array total value to first ele
        # create a curr_sub_total to trace the total of curr sub range to 0
        # create a var called n to 0 and iterate over the list
        #   update the curr_sub_total by adding n 
        #   update the max_sub_total if curr_sub_total is greater than max_sub_total
        #   check if curr_sub_total < 0:
        #       set curr_sub_total to 0 again
        
        
        max_sub_total = nums[0]
        curr_sub_total = 0
        
        n = 0
        for num in nums:
            curr_sub_total += num
            max_sub_total = max(max_sub_total, curr_sub_total)
            if curr_sub_total < 0:
                curr_sub_total = 0
                
        return max_sub_total
    