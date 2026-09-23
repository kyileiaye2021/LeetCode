class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # happy cases
        # [1,3,5,6], target = 5
        # 2

        # [1,3,5,6], target = 2
        #  1

        # [1,3,5,6], target = 7
        # 3

        # edge cases
        # [4], target = 4
        # 0

        # [4], target = 2
        # 0

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return l
