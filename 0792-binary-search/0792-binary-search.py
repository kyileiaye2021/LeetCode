class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # happy cases
        # input: nums = [1,2,5], target = 2
        # output: 1

        # input: nums = [1], target = 1
        # output: 0

        # edge cases
        # input: nums = [-1,3], target = 0
        # output: -1

        # binary search 
        
        # low level plan
        # 2 pointers i ,j
        # itereate until i passes j
        #   find mid ele
        #   check if the target ele is greater than mid ele
        #       move i by mid + 1
        #   move j by mid -1
        # return mid

        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                i = mid + 1

            else:
                j = mid - 1
        
        return -1
            