class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # happy cases
        # nums = [3,2,3]
        # output: 1

        # nums = [5, 3, 1]
        # output: -1

        # edge cases
        # nums = [4]
        # output: 0

        # nums = [1,0]
        # output: 0

        # nums = [0, 1]
        # output: 1

        # left prefix sum - sum of all ele before ith ele
        # sum all nums - right suffix
        # iterate thru each ele 
        #   subtract ith ele from the right most
        #   check if the left prefix == right suffix
        #       return i
        # return -1

        left_prefix = 0
        right_suffix = sum(nums)
        for i in range(len(nums)):
            right_suffix -= nums[i]
            if left_prefix == right_suffix:
                return i
            left_prefix += nums[i]

        return -1