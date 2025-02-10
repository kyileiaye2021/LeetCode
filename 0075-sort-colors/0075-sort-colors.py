class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # happy case
        # input = [2,2,1,0]
        # output = [0, 1, 2, 2]

        # edge cases
        # input = [0,0]
        # output = [0,0]

        # input = [2]
        # output = [2]

        # forward backword two pointer 
        # iterate thru the list
        #   check if the curr ele is 0 
        #       swap that ele with the ele curr pointed by l
        #       increment l by 1
        #   check if the curr ele is 2
        #       swap that ele with the ele curr pointed by r
        #       decrement r by 1

        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
                i -= 1

            elif nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            i += 1
            
        return nums
        