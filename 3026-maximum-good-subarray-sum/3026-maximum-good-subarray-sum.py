class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # happy cases
        # nums = [1,2,3,4,5,6], k = 1
        # output = 11

        # nums = [-1,3,2,4,5], k = 3
        # output = 11

        # edge cases
        # nums = [2, 1], k = 0
        # output = 0

        # nums = [-1,-2,-3,-4], k = 2
        # output: -6

        # nums = [-1,-2.-3,-3], k = 2  
        # output: -6

        # nums = [1,2,3,3], k = 2
        # output: 9

        # prefix sum + hashmap 
        # hashmap = {ele: prefix sum before that ele}
        # iterate thru all nums ele 
        #   map curr n to prefix sum of curr n
        #   curr prefix = n + curr prefix (including curr n)
        #   if curr n - k in map
        #       curr sum = curr prefix - map[curr n - k]
        #   if curr n + k in map
        #       curr sum = curr prefix - map[curr n + k]
        #   update max_sum = max(max_sum , curr sum)
        # return max_sum

        prefix_before = {}
        curr_prefix = 0
        max_sum = float('-inf')

        for n in nums:
            if n not in prefix_before:
                prefix_before[n] = curr_prefix
            else:
                prefix_before[n] = min(curr_prefix, prefix_before[n])
            curr_prefix += n 
            if n - k in prefix_before:
                curr_sum = curr_prefix - prefix_before[n - k]
                max_sum = max(curr_sum, max_sum)
            if n + k in prefix_before:
                curr_sum = curr_prefix - prefix_before[n + k]
                max_sum = max(curr_sum, max_sum)

        return max_sum if max_sum != float('-inf') else 0