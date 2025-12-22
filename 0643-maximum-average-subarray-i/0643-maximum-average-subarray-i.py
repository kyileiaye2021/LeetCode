class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # find the first k ele sum and avg

        # iterate thru the ele from the second ele
        #   excluding the prev i - 1 value
        #   adding the i + k - 1 value
        #   find the avg and update the avg if needed
        # return the max avg

        max_avg = 0
        total = 0
        for i in range(k):
            total += nums[i]
        curr_avg = total / k
        max_avg = curr_avg

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            curr_avg = total / k
            max_avg = max(max_avg, curr_avg)

        return max_avg