class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        # find which side mid ele fall into 
        # if len(nums) == 1:
        #     return nums[0]
        l = 0
        r = len(nums) - 1
        smallest = float('inf')

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]:
                if nums[l] <= nums[r]:
                    smallest = min(smallest,nums[mid])
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                smallest = min(smallest, nums[mid])
                r = mid - 1

        return smallest

