class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        closet = float('inf')
        res = 0

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_closet = abs(cur_sum - target)
                if closet > cur_closet:
                    closet = min(closet, abs(cur_closet))
                    res = cur_sum

                if cur_sum > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif cur_sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                else:
                    return cur_sum
            
        return res

