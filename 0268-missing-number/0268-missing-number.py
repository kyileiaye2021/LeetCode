class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # sorting
        # O(nlogn) time 

        # sum of 0 to 3 - sum of nums = missing num
        # n = len(nums)
        # total = sum(i for i in range(n + 1))
        # return total - sum(nums)

        res = len(nums)

        for i in range(len(nums)):
            res ^= (i ^ nums[i])

        return res


        