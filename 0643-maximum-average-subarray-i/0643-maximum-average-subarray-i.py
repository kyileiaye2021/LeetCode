class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        total = 0
        max_avg = float('-inf')

        for i in range(k): # first k total and avg
            total += nums[i]
            avg = total / k
        max_avg = max(max_avg, avg)

        l = 0
        for r in range(k, len(nums)):
            total += nums[r] 
            total -= nums[l]
            l += 1
            avg = total / k
            max_avg = max(max_avg, avg)

        return max_avg


        