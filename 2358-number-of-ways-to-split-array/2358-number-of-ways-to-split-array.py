class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        # find sum of all ele
        # count = 0
        # iterate thru the nums upto second to last ele
        #   increment curr total by adding ith position
        #   subtract curr ith value from sum
        #   check if the curr total >= sum
        #       increment the count
        # return count

        total_sum = sum(nums)
        count = 0
        curr_total = 0
        for i in range(len(nums) - 1):
            curr_total += nums[i]
            total_sum -= nums[i]
            if curr_total >= total_sum:
                count += 1

        return count
        