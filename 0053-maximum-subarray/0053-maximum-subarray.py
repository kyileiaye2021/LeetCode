class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # sliding window approach
        # if curr sum becomes negative, reset to 0
        # update the max sum with current sum
        # return the max sum

        max_sum = nums[0]
        curr_sum = 0

        for ele in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += ele
            max_sum = max(max_sum, curr_sum)

        return max_sum

        