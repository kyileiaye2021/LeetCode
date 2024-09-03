class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # happy cases
        # input - [2,0,2,1,1,0]
        # output - [0,0,1,1,2,2]
        
        # edge cases
        # input - [0]
        # output - [0]
        # input - [1]
        # output - [1]
        # input - [2]
        # output - [2]
        
        # counting ele approach
        # partition approach
        
        # partition approach
        # create two pointers l, r
        # start i from 0
        # iterate over the list until i passes r
        #   check if the curr ele is 0
        #       swap the curr ele with the ele that is curr pointed by l pointer
        #       increment l by 1
        #   else if the curr ele is 2
        #       swap the curr ele with the ele that is curr pointed by r pointer
        #       decrement r by 1
        #       decrement i by 1
        #   increment i by 1
        
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
                i -= 1
                
            i += 1
            