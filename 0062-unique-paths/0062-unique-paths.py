class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def dfs (i, j)
        # if i == m - 1 and j == n - 1:
        #   return 1
        # if i == m:
        #   return 0
        # if j == n:
        #   return 0

        # d = dfs(i + 1, j) go down
        # r = dfs(i , j + 1) go right
        # return d + r

        memo = {}
        def dfs(i, j):
            # if reach the bottom right position
            if i == m - 1 and j == n - 1:
                return 1
            
            if i >= m: # if i exceeds curr row, can't go down and cannot reach the goal
                return 0
            
            if j >= n: # if j exceeds curr len, can't go right anymore and cannot reach the goal
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            d = dfs(i + 1, j) # go down
            r = dfs(i, j +1) # go right

            memo[(i, j)] = d + r
            return memo[(i, j)]

        return dfs(0, 0)
        