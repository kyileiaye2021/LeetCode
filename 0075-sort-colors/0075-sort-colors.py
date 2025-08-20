class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # l, r = 0, len(nums) - 1
        # iterate thru the list
        #   when we meet 2, replace with r pointer ele 
        #       decrement r pointer
        #   when we meet 0, replace with l pointer ele
        #       increment l pointer

        i = 0
        l = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1

            elif nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
                i += 1

            else:
                i += 1

        

        