class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            
            nonlocal count
            count += 1
            grid[r][c] = 0
            
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        
        count = 0
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, count)
                    count = 0
                
        return max_area
                    