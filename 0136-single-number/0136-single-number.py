class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # [4,4,2]
        # output: 2

        # [1,2,2]
        # output: 1

        # [7,6,6,1,1]
        # output: 7
        # hashmap : O(n) space
        # sort and traverse : O(nlogn) time
        # bucket sort like storing the count at each index : O(n) space

        res = 0

        for n in nums:
            res ^= n

        return res

        