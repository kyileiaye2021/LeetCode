class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # happy case
        # input: [0, 1, 0]
        # output: [1, 0, 0]

        # edge cases
        # input: [0, 0]
        # output: [0, 0]

        # input: [1]
        # output: [1]

        # Brute force (O(n))
        # Dictionary (O(n))
        # Two pointer (O(n))

        # low level steps 
        # initialize two pointers i and j
        # i, j = 0, 0
        # iterate over the list until i reaches the end of the lst
        #   check if the i ele is not 0
        #       assign the i ele in the j position 
        #       increment both i and j by 1
        #   increment i
        # iterate over the list from jth position to the end of the list
        #   assign the value of cur ele to 0

        i, j = 0, 0

        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1

