class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 3 triplets -> distinct
        # nested loops -> O(n^3)

        nums.sort()
        # iterate thru the ele 
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur_ele = nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if cur_ele + nums[l] + nums[r] > 0:
                    r -= 1

                elif cur_ele + nums[l] + nums[r] < 0:
                    l += 1

                else:
                    res.append([cur_ele, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1

        return res

