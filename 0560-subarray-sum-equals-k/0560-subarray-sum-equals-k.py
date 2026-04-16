class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_count = {0:1}
        res = 0
        prefix_sum = 0

        for n in nums:
            prefix_sum += n

            if prefix_sum - k in prefix_count:
                res += prefix_count[prefix_sum - k]
            
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return res

            
