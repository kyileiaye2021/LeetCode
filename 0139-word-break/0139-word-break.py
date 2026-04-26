class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # check char by char
        # if l not in wordDict -> go to le -> not in wordDict -> keep going
        # leet in wordDict -> call recursive func on the remaining chars

        # dfs(i)
        # if i == len(s):
        #   need to stop -> return true
        # if memo[i]: return memo[i]
        # for j in range(i, len(s)):
        #   if s[:i] in wordDict
        #       memo[i] = dfs(i + 1)
        # return memo[i]
        memo = {}
        def dfs(i):
            if i == len(s):
                return True # if reach the last index,valid split 

            if i in memo:
                return memo[i]

            for j in range(i, len(s)):
                # if the substr up to i is not in wordDict, keep going
                # else check the remaining substr is in wordDict
                cur_word = s[i:j + 1]
                if cur_word in wordDict: 
                    if dfs(j + 1):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]

        return dfs(0)