class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def helper(nums):
            first = 0
            second = 0

            for n in nums:
                temp = max(first + n, second)
                first = second
                second = temp

            return second

        max1 = helper(nums1)
        max2 = helper(nums2)

        return max(max1, max2)
        