class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointers 
        # l and r
        # res
        # while l < r
        #   square both l and r
        #   if r ele square > l ele square
        #       adding l ele square to res
        #   else
        #       add r ele square to res
        # return res

        res = [0] * len(nums)
        i = len(nums) - 1
        l = 0
        r = len(nums) - 1

        while l <= r:
            left_squared = nums[l] ** 2
            right_squared = nums[r] ** 2
            if right_squared > left_squared:
                res[i] = right_squared
                r -= 1
            else:
                res[i] = left_squared
                l += 1
            i -= 1

        return res
        
        # [100]
        # [16,100]
        # [9, 16, 100]
        # [1, 9, 16, 100]
        # [0, 1, 9, 16, 100]