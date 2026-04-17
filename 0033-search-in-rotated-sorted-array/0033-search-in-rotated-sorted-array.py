class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if mid val >= l ele
        #   left side
        #   if target > mid
        #       l = mid + 1
        #   elif target < mid
        #       if target < l ele
        #           l = mid + 1
        #   else
        #       return mid
        # else:
        #   right side
        #   if target > mid
        #       if target > r ele
        #           r = mid -1
        #       else:
        #           l = mid + 1
        #   elif target < mid
        #       r = mid - 1
        #   else:
        #       return mid
        # return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[l]:
                # left side
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
    
                else:
                    r = mid - 1
               
            else:
                # right side
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                
                else:
                    l = mid + 1

        
        return -1
