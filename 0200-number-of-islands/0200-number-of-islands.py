class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # [[1,1,0,1]]
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        islands = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return
            if grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands += 1
                    dfs(i, j)
        return islands
