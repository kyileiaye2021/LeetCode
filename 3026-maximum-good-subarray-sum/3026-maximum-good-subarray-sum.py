class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_before = {}
        cur_prefix = 0
        max_sum = float('-inf')

        for n in nums:
            if n not in prefix_sum_before:
                prefix_sum_before[n] = cur_prefix

            else:
                prefix_sum_before[n] = min(cur_prefix, prefix_sum_before[n])
            cur_prefix += n

            if n - k in prefix_sum_before:
                cur_sum = cur_prefix - prefix_sum_before[n - k]
                max_sum = max(max_sum, cur_sum)

            if n + k in prefix_sum_before:
                cur_sum = cur_prefix - prefix_sum_before[n + k]
                max_sum = max(max_sum, cur_sum)

        return max_sum if max_sum != float('-inf') else 0

