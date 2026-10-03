class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # happy cases
        # nums = [1,2,3,4]
        # [24,12,8,6]

        # # nums = [-1,1,0,-3,3]
        # [0,0,9,0,0]

        # edge cases
        # nums = [4,5]
        # [5, 4]

        # nums = [1,1]
        # [1,1]

        # brute force 
        # nested for loop
        # O(n^2) time

        # prefix and postfix products O(n) time
        # O(n) space

        # prefix 
        # postfix

        pre = 1
        pos = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * pos
            pos = pos * nums[i]

        return res



        
        
