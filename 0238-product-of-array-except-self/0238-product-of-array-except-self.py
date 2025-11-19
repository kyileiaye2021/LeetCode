class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # happy cases
        # nums = [1,2,3,4]
        # output  = [24, 12, 8, 6]

        # edge cases
        # nums = []
        # output: []

        # nums = [2, 0]
        # output: [0, 2]

        # nums = [-1, -1, -1]
        # output: [1, 1, 1]

        # nums = [-1, 0, -2]
        # output: [0, 2, 0]

        # brute force
        # nested loop (O(n^2))

        # prefix sum 2 arrays O(n) time , O(n) space
        # prefix sum var left, and right

        left = 1
        right = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left
            left = left * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right = right * nums[i]

        return res
    