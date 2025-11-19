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

        left = [1] * len(nums)
        left[0] = nums[0]
        right = [1] * len(nums)
        right[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        for i in range(len(nums)):
            if 0 < i < len(nums) - 1:
                nums[i] = left[i - 1] * right[i + 1]
            if i == 0:
                nums[i] = right[i + 1]
            if i == len(nums) - 1:
                nums[i] = left[i - 1]

        return nums