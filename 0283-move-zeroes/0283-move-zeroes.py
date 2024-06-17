class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #create a pointer to keep track of the index of the elements which is not zero
        #iterate over the list
        #check the current ele is zero or not
        #if it's , assign the ele into whatever the created pointer is and increment the pointer by 1
        #if it's not, bypass to next ele
        #length of the list - not_zero_index to get length of the rest in the list
        #iterate over that amount of length to replace the value with 0

        not_zero_index = 0
        for ele in nums:
            if ele != 0:
                nums[not_zero_index] = ele
                not_zero_index += 1

        rest_length = len(nums) - not_zero_index

        for i in range(rest_length):
            nums[not_zero_index] = 0
            not_zero_index += 1



        