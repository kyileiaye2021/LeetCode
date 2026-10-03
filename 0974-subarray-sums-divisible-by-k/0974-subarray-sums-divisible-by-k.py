class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_count = {0:1}
        res = 0 # num of subarr
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            if prefix_sum % k in prefix_count:
                res += prefix_count[prefix_sum % k]

            prefix_count[prefix_sum % k] = 1 + prefix_count.get(prefix_sum % k, 0)
        return res
