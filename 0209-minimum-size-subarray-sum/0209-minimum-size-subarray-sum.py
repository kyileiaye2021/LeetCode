class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # brute force
        # sliding window with 2 pointers
        # i , j 
        # if reach the target: return window size
        # if exceed the target: chop off the first ele until the subarray sum becomes target
        
        # [1, 4, 4]
        # target = 4
        # output: 1

        # [1,2,2,4]
        # target = 4
        # output: 1

        l = 0
        total = 0
        min_window = float('inf')
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_window = min(min_window, r - l + 1)
                total -= nums[l]
                l += 1

        return min_window if min_window != float('inf') else 0
