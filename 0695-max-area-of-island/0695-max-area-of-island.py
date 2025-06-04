class Solution:
    def dfs(self, grid, r, c):

        grid[r][c] = 0
        count = 1

        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        for dir_r, dir_c in directions:
            new_r = r + dir_r
            new_c = c + dir_c
            if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c]== 1:
                grid[new_r][new_c] = 0
                count += self.dfs(grid, new_r, new_c)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        # mark the curr cell as 0
        # go to the neighbor in 4 directions and mark them as 0
        #   count incremented

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.dfs(grid,r, c)
                    max_area = max(max_area, area)

        return max_area

