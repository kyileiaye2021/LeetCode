class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        i = len(nums) - 1

        while l <= r:
            l_ele = nums[l] ** 2
            r_ele = nums[r] ** 2

            if l_ele < r_ele:
                res[i] = r_ele
                r -= 1

            else:
                res[i] = l_ele
                l += 1

            i -= 1

        return res

            


        