class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        min_window = float('inf')

        while r < len(nums):
                    
            total += nums[r]
            if total >= target:
                curr_window = r - l + 1
                min_window = min(curr_window, min_window)
                # total -= nums[l]
                # l += 1

            while total >= target:

                total -= nums[l]
                l += 1

                # check again if total is still greater than target after shrinking the window size
                if total >= target:
                    curr_window = r - l + 1
                    min_window = min(curr_window, min_window)

            r += 1

        return 0 if min_window == float('inf') else min_window

