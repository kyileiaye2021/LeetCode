class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # happy cases
        # nums = [1,0,-1,0,-2,2], target = 0
        # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        # nums = [-1,0,1,0,8,-8,8,-8], target = 0
        # [[-1,0,1,0],[8,8,-8,-8], [8,-8,0,0], [8,-8,-1,1]]

        # nums = [1,2,3,4], target = 10
        # [[1,2,3,4]]

        # edge cases
        # nums = [2,2,2,2,2], target = 8
        # [[2,2,2,2]]

        # nums = [2,2,2,2,2], target = 10
        # []

        # nums = [2,2,2], target = 8
        # []

        # sort the nums 
        # iterate thru nums with i upto len(nums) - 3 
        #   negage curr ith ele (target)
        #   iterate thru nums with j (i + 1) - 2
        #       l = j + 1, r = last ele
        #       while l < r
        #           curr sum = l ele + r ele + curr i ele
        #           if curr sum == target
        #               add that [curr i ele, curr j ele, l ele, r ele ] to the res
        #               l and r pointer by 1
        #               while l ele == l -1 ele, increment l by 1
        #               while r lele == r + 1 ele, decrement r by 1
        #           if curr sum < target:
        #               increment l by 1
        #               while l ele == l -1 ele, increment l by 1
        #           if curr sum > target
        #               decrement r by 1
        #               while r lele == r + 1 ele, decrement r by 1
        #       j += 1
        #       while j elel == j - 1 ele
        #           j += 1

        #   i += 1
        #   whilie i ele == i - 1 ele
        #       i + = 1

        # nums.sort()
        # res = []

        # i = 0
        # while i < len(nums) - 3:
        #     j = i + 1
        #     while j < len(nums) - 2:
        #         l = j + 1
        #         r = len(nums) - 1

        #         while l < r:
        #             curr_sum = nums[l] + nums[r] + nums[j] + nums[i]

        #             if curr_sum == target:
        #                 res.append([nums[l], nums[r], nums[i], nums[j]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1
        #                 r -= 1
        #                 while l < r and nums[r] == nums[r + 1]:
        #                     r -= 1

        #             elif curr_sum > target:
        #                 r -= 1
        #                 while l < r and nums[r] == nums[r + 1]:
        #                     r -= 1

        #             else:
        #                 l += 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1

        #         j += 1
        #         while j < len(nums) and nums[j] == nums[j - 1]:
        #             j += 1

        #     i += 1
        #     while i < len(nums) and nums[i] == nums[i - 1]:
        #         i += 1

        # return res

        nums.sort()
        res = []
        quad = []

        def recur_sum(k, idx, target):

            # base case
            if k == 2:
                # 2 sum
                l = idx
                r = len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif nums[l] + nums[r] > target:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1 
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                

            else:
                while idx < len(nums) - k + 1:
                    quad.append(nums[idx])
                    recur_sum(k - 1, idx + 1, target - nums[idx])
                    quad.pop()

                    idx += 1
                    while idx < len(nums) and nums[idx] == nums[idx - 1]:
                        idx += 1
            
        recur_sum(4, 0, target)
        return res



