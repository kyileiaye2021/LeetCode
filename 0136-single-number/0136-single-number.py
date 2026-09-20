class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # sort and iteration pass
        # O(nlogn)

        # set
        # O(n) time and O(n) space

        # XOR
        # O(n) time and O(1) space

        res = 0
        for n in nums:
            res ^= n
        return res
        