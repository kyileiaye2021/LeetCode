class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # happy cases
        # [0,1,0,3,12]
        # [1,3,12,0,0]

        # [-1,2,0,3]
        # [-1,2,3,0]

        # [9,2]
        # [9,2]

        # edge cases
        # [0,0,0]
        # [0,0,0]

        # [1,0]
        # [1,0]

        # 2 pointers
        # i , j
        # iterate thru the ele with j
        #   if j ele is not 0
        #       i ele = j ele
        #       i += 1
        #   j += 1
        # start form i
        #   iterate thru remaining ele and change to 0
        

        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

            j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1



        