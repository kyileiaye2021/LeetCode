class Solution:
    def findMin(self, nums: List[int]) -> int:
        # happy cawe
        # nums = [3,4,5,6,1,2]
        # output: 1

        # nums = [4,5,0,1,2,3]
        # output: 0

        # nums = [11,12,13]
        # output: 11

        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:

            # if we get totally sorted arr
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]: # in left portion
                l = mid + 1 # so find in right

            else: # in right portion
                r = mid - 1 # so find in left

        return res