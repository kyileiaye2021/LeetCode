class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Happy case
        # input - nums=[3,2,2,3], and val = 3
        # output - 2 , [2,2,_,_]
        
        # Edge case
        # input - nums=[], and val = 2
        # output - 0, []
        
        # input - nums=[3,4,5], val = 2
        # output - 3, [3,4,5]
        
        
        # Two pointer approach
        # create two pointer p and q
        # iterate until p reaches the end of the nums list
        #   check if p ele is not the same as val
        #       assign p ele to the position where q is curr pointing to
        #       increment q by 1
        #   increment p by 1
        # return q
        
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        p, q = 0, 0
        while p < len(nums):
            if nums[p] != val:
                nums[q] = nums[p]
                q += 1
            p += 1
            
        return q