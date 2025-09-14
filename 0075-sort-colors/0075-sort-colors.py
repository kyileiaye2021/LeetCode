class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # happy cases
        # input: nums = [1,2,0,2,1]
        # output: [0,1,1,2,2]

        # input: nums = [2,1,0,2,2]
        # output: [0, 1,,2,2,2]

        # edge cases
        # input: [2,0,1]
        # output: [0,1,2]

        # input: []
        # output: []

        # brute force (nested for loop)
        # two pointers - i, j
        # iterate thru the list with k
        #   if curr ele is 0
        #       swap with ith position 
        #       increment i by 1
        #       decrement k by 1
        #   elif curr ele is 2
        #       swap with jth position 
        #       decrement j by 1
        #       decrement k by 1
        #   increment k by 1

        i = 0
        j = len(nums) - 1
        k = 0

        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1

            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                k -= 1
            
            k += 1

        
        
