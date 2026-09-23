class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # finding the last occurence of target in nums
        l = 0
        r = len(nums) - 1
        last_idx = -1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                last_idx = mid
                l = mid + 1

        first_idx = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1

            else:
                first_idx = mid
                r = mid - 1            

        return [first_idx, last_idx]
        # find first occurence of target in nums
        