class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # prefix (keep track of both max and min)
        # largest product = max(nums)

        # iterate thru the nums
        #   product of current n and max
        #   product of current n and min
        #   update max and min
        #   if curr n == 0 reset max and min to 1
        #   update largest product so far

        res = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1

            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(res, curMax, curMin)

        return res
            