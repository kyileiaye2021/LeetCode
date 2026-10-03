class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)

        while l <= r:
            mid = (l + r) // 2

            if mid - 1 < 0 and mid + 1 >= len(nums):
                return mid

            if mid - 1 < 0:
                if nums[mid + 1] > nums[mid]:
                    return mid + 1
                else:
                    return mid

            if mid + 1 >= len(nums):
                if nums[mid - 1] > nums[mid]:
                    return mid - 1

                else: 
                    return mid

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid - 1] < nums[mid + 1]:
                l = mid + 1

            else:
                r = mid - 1

            
