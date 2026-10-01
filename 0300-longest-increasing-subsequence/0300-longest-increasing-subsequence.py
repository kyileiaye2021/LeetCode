class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        # dfs (memoization)
        # recur(i, curlist)
        # base case
        #   if i >= len(nums) or curr i ele < curlist[-1]
        #       return len(curlist)

        # recursive case
        #   max_len = 0
        #   for j in range(i + 1, len(nums)):
        #       cur_len = recur(j, nums[i] + [])
        #       max len = max(cur len, max len)
        #   return max len

        # for i in range(len(nums)):
        #   recur(i, [])
        memo = [0] * len(nums)
        def dfs(i):
            if memo[i] > 1:
                return memo[i]
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            memo[i] = best
            return memo[i]
        
        max_res = 0
        for i in range(len(nums)):
            max_res = max(max_res, dfs(i))

        return max_res
