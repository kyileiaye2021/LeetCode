class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # count = 0
        # total = 1
        # l = 0
        # r = 0
        # iterate thru the ele with r
        #     total *= n
        #     
        #     while total >= k:
        #              total = total / l ele 
        #              l += 1
        #     count += r -l + 1
        #   r += 1
        # return count

        count = 0
        total = 1
        l = 0
        r = 0

        while r < len(nums):
            total *= nums[r]

            while l <= r and total >= k:
                total = total / nums[l]
                l += 1

            count += (r - l + 1)

            r += 1
        return count