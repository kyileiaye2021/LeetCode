class Solution:
    def numDecodings(self, s: str) -> int:
        # recur(i)
        # base case
        #   if i >= len(s)
        #       return 1
        #   if s[i] == 0:
        #       return 0
        # recursive case
        #.  res = recur(i + 1)
        #   ## taking 2 digits
        #   if i + 1 < len(nums) and s[i] == 1 or s[i] == 2 and s[i + 1] in '0123456'
        #       res += recur(i + 2)
        #   return res

        memo = {}

        def recur(i):
            #base case
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0

            # recursive case
            if i in memo:
                return memo[i]

            res = recur(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                res += recur(i + 2)

            memo[i] = res
            return memo[i]

        return recur(0)