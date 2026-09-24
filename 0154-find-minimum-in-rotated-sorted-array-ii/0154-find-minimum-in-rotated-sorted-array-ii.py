class Solution:
    def findMin(self, nums: list[int]) -> int:
        # binary search

        # l = 0
        # r = len(nums) - 1
        # while l < = r
        #   
        #   if l ele <= r ele
        #       return l ele
        #   mid = l + ((r - l) // 2)
        #   if mid ele >= l ele
        #       l = mid + 1
        #   else
        #       res = mid
        #       r = mid - 1
        
        # return res

        l = 0
        r = len(nums) - 1
        res = float('inf')
        while l <= r:

            mid = l + ((r - l) // 2)

            if nums[l] == nums[mid]:
                res = min(res, nums[mid])
                l += 1

            elif nums[l] > nums[mid]:
                res = min(res, nums[mid])
                r = mid - 1

            else:
                if nums[r] > nums[l]:
                    # return nums[l]
                    return min(res, nums[l])

                else:
                    l = mid + 1

        return res

