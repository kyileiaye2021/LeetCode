class Solution:
    def dfs(self, r, c, grid, count, dirs):
        grid[r][c] = 0
        count[0] += 1

        for dx, dy in dirs:
            new_r, new_c = r + dx, c + dy
            if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == 1:
                self.dfs(new_r, new_c, grid, count, dirs)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = [0]
                    self.dfs(r, c, grid, count, dirs)
                    max_count = max(max_count, count[0])

        return max_count
                    

       