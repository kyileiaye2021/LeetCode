class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 2 pointers
        
        # i , j
        
        i, j = 1, 1

        while j < len(nums):

            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i
        