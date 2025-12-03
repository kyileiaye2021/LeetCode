class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [3,2,3,2], val = 3
        # output: [2,2], 2

        # nums = [], val = 3
        # output: [], 0

        # nums = [1,2,3] val = 4
        # output: [1,2,3], 3

        # two pointers

        # i - maintain the index postion where the ele is not equal to val
        # j - the iterator 
        # 
        # iterate thru the ele
        #   if curr ele = val
        #       move j by 1
        #   else
        #       assign j ele to i
        #       move i by 1 
        #       move j by 1
        # return i

        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i