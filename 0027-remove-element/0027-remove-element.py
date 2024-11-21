class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # happy cases
        # input: [3,2,2,3], val = 3
        # output: 2,  [2,2]

        # edge cases
        # input: [], val = 1
        # output: 0, []
        # input: [1], val = 1
        # output: 0, []

        # brute force
        # two pointer 

        # low level steps
        # initialize two pointers to 0 (i, j)
        # iterate over the list until i reaches to the end of the list
        #   check if the i ele is not equal to the val
        #       increment both i and j by 1
        #   else:: increment i by 1
        # return j

        i, j = 0, 0

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j
