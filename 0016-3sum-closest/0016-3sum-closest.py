class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        # happy cases
        # nums = [-1,2,1,-4], target = 1
        # -1, 2,1 = 0
        # -1, 2, -4 = -3
        # -1, 1, -4 = -4
        # 2, 1, -4 = -1
        # [-1, 2, 1] = 2

        # nums = [-1, 1, 2, 3], target = 4
        # [-1, 1, 2] = 2

        # nums = [-1, 1, -1, 1], target = 3
        # [-1, 1, -1] = -1
        # [1, -1, 1] = 1
        # 1

        # edge cases
        # nums = [-1, 4, 3], t = 6
        # 6

        # nums = [0,0,0], t = 3
        # 0

        # sorting , 2 pointer 
        # min dist = inf
        # iteate thru the ele starting from i
        #   l and r
        #   while l < r
        #       if l ele + r ele + curr i ele == target, return target
        #       if curr sum = l ele + r ele + curr i ele > target, move r to left
        #           target - curr sum < min dist
        #           update min dist 
        #           if r ele is still the same, move r to left
        #       curr sum = l ele + r ele + curr i ele 
        #           update min dist if target - curr sum < min dist
        #           if curr sum < target, mover l to right
        #           if l ele is still the same, move l to right
        #  i += 1
        #  if prev i ele == curr i ele 
        #  i += 1
    
        # return min dist

        nums.sort()
        min_dist = float('inf')
        res = 0

        i = 0
        while i < len(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                curr_dist = abs(target - curr_sum)
                if min_dist > curr_dist:
                    min_dist = curr_dist
                    res = curr_sum

                if curr_sum == target:
                    return target

                elif curr_sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                else:
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

        return res










