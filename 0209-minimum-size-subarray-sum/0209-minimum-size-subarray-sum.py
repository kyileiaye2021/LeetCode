class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # happy case
        # input: target = 2, nums = [1,1,1]
        # output: 2

        # edge case
        # input: target = 2, nums = [1, 2]
        # output: 1

        # input: target = 10, nums = [1,3,1,5]
        # output: 0

        # Brute Force - nested loop (O(n^2))
        # Sliding window - O(n)
        
        # l,r
        # initialize sum to keep track of the sum of the curr window
        # length to keep track of minimal length
        # curr_len to keep track of the curr window's length
        # iterate thru the list until r passes the len of the list
        #   add the curr r ele to the sum
        #   check if the sum is greater than or equal to target
        #       update the len
        #       exclude the left pointer ele from the sum
        #       increment l by 1
        #   else:
        #       increment curr_len by 1
        #       increment r by 1
        # return minimal len

        l, r = 0, 0
        total = 0
        min_len = float("inf")
        curr_len = 0

        while r < len(nums):
            
            total += nums[r]
            curr_len += 1
            r += 1

            while total >= target:
                min_len = min(min_len, curr_len)
                total -= nums[l]
                l += 1
                curr_len -= 1
   
        if min_len <= len(nums):
            return min_len
        
        return 0
