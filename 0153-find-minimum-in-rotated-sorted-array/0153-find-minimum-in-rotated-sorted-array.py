class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r] or len(nums) == 1:
            return nums[l] # if not rotated, return first ele

        while l < r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]: # mid on the left side
                if nums[l] > nums[r]:
                    l = mid + 1
                else:
                    r = mid 

            else:
                r = mid

        return nums[r]
        

