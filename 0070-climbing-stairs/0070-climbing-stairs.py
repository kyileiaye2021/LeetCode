class Solution:
    def climbStairs(self, n: int) -> int:

        # base case
        # if n is 1 or 2 return n
        # call recursive func on the n - 1 and n -2

        # def recur(n):
        #     if n == 1 or n == 2:
        #         return n

        #     return recur(n - 1) + recur(n - 2)
        
        # return recur(n)

        # memoization
        def recur(n, memo):
            # base case
            if n == 1 or n == 2:
                return n

            if memo[n] != -1:
                return memo[n]

            memo[n] = recur(n - 1, memo) + recur(n - 2, memo)
            return memo[n]

        memo = [-1] * (n + 1)
        return recur(n, memo)

        
        