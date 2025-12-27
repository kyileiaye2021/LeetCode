class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # largest ele smaller than target
        # smallest ele greater than target

        # [-4, -1, -1, 1, 2]
        # target = 1
        # -4 -> total closet -1
        # -1 -> total 2
        # 1 

        # sort the arr
        # iterate thu the arr
        #   curr ele 
        #   l ele , r ele
        #   if total < target
        #       l += 1
        #   elif total > target:
        #       r += 1
        #   elif total == target
        #       l += 1
        #       r -= 1
        # find the diff between target and total
        #       update the most closet diff
        # return the most closet diff sum

        nums.sort()
        closet_sum = float("inf")
        closet_diff = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + curr
                diff = abs(total - target)
                if diff < closet_diff:
                    closet_diff = diff
                    closet_sum = total
                

                if total < target:
                    l += 1

                elif total > target:
                    r -= 1

                else:
                    l += 1
                    r -= 1

                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1

        return closet_sum
        # -4, -1, 1, 2

        # -4 -> -1 closet sum -1 closet diff 2
        # -1 -> closet sum 2 closet diff 1

