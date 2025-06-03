class Solution:

    def dfs(self, grid, r, c):
        # mark the curr entry as visited
        # for each direction 
        #   check if the entry within the bound
        #       check if it's 1 and not visited
        #           call dfs on the neighbor
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        grid[r][c] = 0
        for dir_r, dir_c in directions:
            new_r, new_c = r + dir_r, c + dir_c
            if new_r in range(len(grid)) and new_c in range(len(grid[0])):
                if grid[new_r][new_c] == '1':
                    self.dfs(grid, new_r, new_c)

    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs 
        # for each row in the grid
        #   for each col in the grid
        #       check if the curr entry is 1 and not visited
        #           call dfs
        #           increment island count
        # return island count
        num_island = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    num_island += 1
        return num_island