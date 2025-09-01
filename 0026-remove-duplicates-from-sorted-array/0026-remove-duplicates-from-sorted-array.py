class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [1,1,2]
        # output: 2, nums = [1,2,_]

        # nums = [0,0,1,1,1,1,2,]
        # output: 3, [0,1,2,_]

        # two pointer

        # i, j index 0
        # iterate thry the nums upto 2nd to last ele with j
        #   if j ele is != j + 1 ele
        #       move j ele to i
        #       move i by 1
        #   move j by 1

        i, j = 1, 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i

        