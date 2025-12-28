class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red - 0
        # white = 1
        # blue - 2

        # input: [2,0,1]
        # output: [0,1,2]

        # input: [2,0,1,2]
        # output: [0,1,2,2]

        # input; [1,1,1,0]
        # output: [0,1,1,1]

        # input: [2]
        # output: [2]

        # two pointers
        # l r
        # l - index for 0
        # r = index for 2
        # l = 0, r = len(nums) - 1
        # i = curr index
        # iterate thru the arr
        #   check if curr ele is 2
        #       swap with the curr ele and r pointer ele
        #       r -= 1
        #   check if curr ele is 0
        #       swap with curr ele and l pointer ele
        #       l += 1
        #       i += 1
        
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            else:
                i += 1
        
        # [0,2,1] i = 0, l = 0, r = 2
        # [0,2,1] i = 1, l = 1, r = 2
        # [0,1,2] i = 1, l = 1, r = 1
        # [0,1,2], i = 2, l = 1, r = 1
        


        