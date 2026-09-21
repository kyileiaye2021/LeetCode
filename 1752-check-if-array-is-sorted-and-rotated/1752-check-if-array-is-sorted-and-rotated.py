class Solution:
    def check(self, nums: list[int]) -> bool:
        # happy cases
        # [1,2,3,4,5]
        # true

        # [3,4,5,1,2]
        # true

        # [2, 3,1,4]
        # false

        # [2,2,2,2]
        # true

        # [5,2,2,2]
        # true

        j = 1
        n = 1
        if len(nums) == 1:
            return True
        while j < 2 * len(nums):
            if nums[j % len(nums)] >= nums[(j - 1) % len(nums)]:
                n += 1

            else:
                i = j
                n = 1

            if n == len(nums):
                return True
            
            j += 1
        return False

