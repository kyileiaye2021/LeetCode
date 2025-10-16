class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window
        # prefix sum
        # we can't slide the window by chopping off the prev ele as the negative nums are also included
        
        hashmap = {0: 1} # prefix sum : count
        curSum = 0
        res = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k 

            if diff in hashmap:
                res += hashmap[diff]

            hashmap[curSum] = 1 + hashmap.get(curSum, 0)

        return res
