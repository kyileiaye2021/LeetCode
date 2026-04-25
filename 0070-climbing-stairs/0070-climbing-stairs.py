class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: 
            return n
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        def dfs(n):
            if n == 1 or n == 2:
                return ways[n]

            if ways[n] > 0:
                return ways[n]

            ways[n] = dfs(n - 1) + dfs(n - 2)      
            return ways[n]  

        return dfs(n)