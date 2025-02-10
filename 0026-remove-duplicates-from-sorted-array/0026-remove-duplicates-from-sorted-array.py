class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # happy case
        # input - [1,2,2,4,5]
        # output - [1,2,4,5,_] , 4

        # edge case
        # input - [1,1,1,1]
        # output - [1,_,_,_], 1

        # Brute Force
        # Two pointer 

        i, j = 1, 1

        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

            j += 1

        return i

        
        