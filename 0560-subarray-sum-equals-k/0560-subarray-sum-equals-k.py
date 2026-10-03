class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # edge cases
        # [3,4], k =2
        # 0

        # [-2,1,4,5], k = 9
        # 1

        # [-1,0,1,1,0], k = 0
        # 3

        # sliding window
        # bc of neg nums won't work
        # prefix hashmap

        prefix_count = {0: 1}
        prefix_sum = 0
        res = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_count:
                res += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = 1 + prefix_count.get(prefix_sum, 0)

        return res
