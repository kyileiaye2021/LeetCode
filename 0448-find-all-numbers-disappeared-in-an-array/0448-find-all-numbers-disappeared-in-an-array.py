class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # happy cases
        # nums = [1,2,3,5,5]
        # output: [4]

        # nums = [3,5,6,1,3,3]
        # output: [2,4]

        # nums = [1,1,1]
        # output: [2,3]

        # nums = [1]
        # output: []
    
        # create a set from 1 to n
        # iterate thru the ele in the nums
        #   remove the ele if nums is in set
        # convert the set to list and return 

        n = len(nums)
        nums_list = [i for i in range(1, n + 1)]
        nums_set = set(nums_list)

        for i in range(len(nums)):
            if nums[i] in nums_set:
                nums_set.remove(nums[i])

        return list(nums_set)
