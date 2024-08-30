class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity - O(n)
        # Space complexity - O(1) 
        
        # Happy cases
        # input - [0,1,0,3,12]
        # output - [1,3,12, 0,0]
        
        #Edge cases
        # input - []
        # output - []
        #input - [0]
        # output - [0]
        
        # Two pointer approach
        # p, q pointing to 0, 0
        # iterate over the list until p exceeds the end
        #   check if the curr p pointer ele is not 0
        #       assign the p pointer ele in the pos where q is currently pointing to
        #       increment p and q by 1
        #   else:
        #       increment p by 1
        # replace the ele with 0s starting from q pointer index to the end
        # return the list
        
        p, q = 0, 0
        while p < len(nums):
            if nums[p] != 0:
                nums[q] = nums[p]
                q += 1
            p += 1
        
        while q < len(nums):
            nums[q] = 0
            q += 1
            
        return nums