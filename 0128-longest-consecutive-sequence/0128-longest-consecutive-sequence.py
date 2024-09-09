class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Happy case:
        # input - nums = [100,200,1,2,3]
        # output - 3
        
        # Edge cases:
        # input - nums = []
        # output - 0
        # input - nums = [1]
        # output - 1
        # input - nums = [1, 0, 0]
        # output - 2
        
        # O(n)
        # create a set for the nums
        # create a var longest to trace the longest seq
        # iterate over the ele in the nums
        #   check if ele - 1 is not in the set
        #       y = ele + 1
        #       check while y is in the set
        #           increment y by 1
        #       update the longest
        # return longest
        
        numSet = set(nums)
        longest = 0
        
        for ele in nums:
            if ele - 1 not in numSet:
                y = 1
                while ele+1 in numSet:
                    y += 1
                    ele = ele + 1
                    
                longest = max(y, longest)
        return longest
                
        
        