class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
            else:
                return 
            
            for dx, dy in directions:
                new_x, new_y = dx + i, dy + j
                dfs(new_x, new_y)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res
