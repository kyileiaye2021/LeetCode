class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two ponters starting from 1
        # f, s
        # while s is less than the len of the list
        #   if s ele is the same as s - 1 ele
        #       move s by 1
        #   else:
        #       assign s ele to f 
        #       move f by 1
        #       move s by 1
        # return f + 1

        if len(nums) == 1:
            return 1
        f, s = 1, 1
        while s < len(nums):
            if nums[s] != nums[s - 1]:
                nums[f] = nums[s]
                f += 1
            s += 1
        # nums = nums[:f]
        return f
