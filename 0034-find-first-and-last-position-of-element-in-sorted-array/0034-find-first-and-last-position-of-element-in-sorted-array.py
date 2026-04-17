class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums = [1,2,3,4], target = 3
        # output: [2,2]

        # nums = [1,2,2,3,4], target = 2
        # output: [1,2]

        # nums = []
        # output: [-1. -1]

        # nums = [1,2,2,2,3,4], target = 2
        # output: [1, 3]

        # l index
        # mid = l + r // 2
        # if mid ele > target
        #   r = mid - 1
        # elif mid ele < target:
        #   l = mid + 1
        # else
        #   left_index = mid
        #   r = mid - 1

        # r index
        # mid = l + r // 2
        # if mid ele > target:
        #   r = mid -1
        # elif mid e.e < target:
        #   l = mid + 1
        # else:
        #   right index = mid
        #   l = mid + 1

        # [2], target = 2
        # [0,0]

        # return [left, right]

        low = 0
        high = len(nums) - 1
        left = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                left = mid
                high = mid - 1

        low = 0
        high = len(nums) - 1
        right = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                right = mid
                low = mid + 1

        return [left, right] 

        





        