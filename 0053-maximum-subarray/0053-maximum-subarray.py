class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if the curr sum becomes lesser than the max, then we have to move left pointer and subtract the left pointer ele from the arr

        # until the right pointer reaches the end
        maxSum = float('-inf')
        currSum = 0

        for ele in nums:
            currSum += ele
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0

        return maxSum