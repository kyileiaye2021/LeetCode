class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # happy cases
        # nums = [1,0,3]
        # output: 2

        # nums = [1]
        # output: 0

        # nums = [0]
        # output: 1

        n = len(nums)
        num_list = [i for i in range(n+1)]
        num_set = set(num_list)

        for i in range(len(nums)):
            if nums[i] in num_set:
                num_set.remove(nums[i])
        
        remaining = num_set.pop()
        return remaining