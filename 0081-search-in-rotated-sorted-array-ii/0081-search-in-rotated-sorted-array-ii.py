class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # while l <= r:
        # mid = (l + r) // 2
        # if mid ele > l ele
        #   if l ele <= target < mid ele: r = mid - 1
        #   else: l = mid + 1
        # elif mid ele < l ele
        #   if if mid ele < target <= r ele: l = mid + 1
        #   else: r = mid - 1
        # else: l += 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return True

            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1

                else: 
                    l = mid + 1

            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1
            
            else:
                l += 1

        return False
