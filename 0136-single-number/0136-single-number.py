class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # XOR => results in 0 if the two operators are the same
        # XOR all ele and total is gonna to the res
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res