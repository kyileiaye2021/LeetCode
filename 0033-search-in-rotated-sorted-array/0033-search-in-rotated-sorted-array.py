class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        # binary search
        # which side mid val falls into
        # if mid val == target
        #   return True
        # if left ele < mid val
        #   mid on left side
        #   if m ele > target
        #       if target < left ele
        #           go to right side (l = mid + 1)
        #       else
        #           go to left side (r = mid - 1)
        #   else
        #       go to right side (l = mid + 1)
        # else: 
        #   mid on the right side
        #   if mid ele > target:
        #       go to left side (r = mid - 1)
        #   else
        #      if target > r ele
        #           go to left side (r = mid - 1)
        #      else
        #           go to right side (l = mid + 1)
        # 
        # return False

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid

            # which side mid val fall into 

            if nums[l] <= nums[mid]: # left side
                if nums[mid] > target:
                    if nums[l] > target:
                        l = mid + 1

                    else:
                        r = mid - 1
                
                else:
                    l = mid + 1
            
            else: # right side
                if nums[mid] < target:
                    if nums[r] < target:
                        r = mid - 1

                    else:
                        l = mid + 1

                else:
                    r = mid - 1

        return -1
