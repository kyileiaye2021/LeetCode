class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # happy cases
        # nums = [1,2,3,1]
        # 2

        # nums = [1,2,1,3,5,6,4]
        # 1

        # edge cases
        # [1,2,1]
        # 1

        # [1]
        # 0

        # [2,1,2]
        # 0

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            else:
                return mid

        