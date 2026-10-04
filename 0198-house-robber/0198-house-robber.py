class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        first = nums[0]
        second = max(nums[1], first)
        
        for i in range(2, len(nums)):
            tmp = second
            second = max(first + nums[i], second)
            first = tmp
        return second