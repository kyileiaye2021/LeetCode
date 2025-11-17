class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if l val <= m val (on the left side)
        #   if l val < r val
        #       r = mid
        #
        #   if l val > r val
        #       l = mid + 1
        # 
        #   if l val == r val
        #       l += 1

        # else ( on the right side)
        #   r = mid

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[l] <= nums[mid]: #  mid on the left side

                if nums[l] < nums[r]:
                    r = mid

                elif nums[l] > nums[r]:
                    l = mid + 1

                else:
                    l += 1

            else: # mid on the right side
                r = mid

        return nums[r]
