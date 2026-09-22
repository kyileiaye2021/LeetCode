class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        # hashmap 
        # longest = 0
        # iterate thru nums with r
        #   if curr n in hashmap
        #       while count[r ele] >= k 
        #           count[l ele] -= 1
        #           l += 1
        #   add n to hashmap
        #   curr win = r - l +1
        #   update longest
        #   r += 1
        # return longest

        count = {}
        longest = 0

        l, r = 0, 0

        while r < len(nums):
            if nums[r] in count:
                while count[nums[r]] >= k:
                    count[nums[l]] -= 1
                    l += 1

            count[nums[r]] = 1 + count.get(nums[r], 0)
            curr_window = r - l + 1
            longest = max(longest, curr_window)
            r += 1
        return longest


        