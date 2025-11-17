class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # happy case
        # input: [4,5,6,7,0,1,2], target = 0
        # output: 4

        # input: [4,5,6,7,0,1,2], target = 4
        # output: 0

        # input: [4,5,6,7,0,1,2], target = 2
        # output: 6

        # edge case
        # input: [4,5,6,7,0,1,2], target = 11
        # output: -1

        # input: [3], target = 3
        # output: 0

        # input: [4,5], target = 9
        # output: -1

        # O(n)
        # binary search
        # while l < r
        # find the mid index value
        #   if mid val is target, return mid index
        # if mid val is > target
        #   if the l val is > target
        #       move mid to the right
        #   else
        #       move mid to the left
        # else
        #   if target < r val
        #       move mid to the right
        #   else
        #       move mid to the left
        # return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # first identify on which side the mid val falls into
            # if mid > l val --> left side
            # if mid < l val --> right side

            if nums[mid] >= nums[l]:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    if target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1

            else: 
                if target > nums[mid]:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                else:
                    r = mid - 1

        return -1

        