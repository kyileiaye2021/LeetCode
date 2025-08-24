class Solution:
    def dfs(self, r, c, grid):
        grid[r][c] = '0'

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dx, dy in dirs:
            new_r = r + dx
            new_c = c + dy

            if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == '1':
                self.dfs(new_r, new_c, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # mark the cell as 0
        # go to neighbors
        # for each neighbor 
        #   check they are within boundary and they are 1
        #       call dfs func on the cell

        # iterate thru the ele in the 2d grid
        #   if the cell is 1 
        #       call dfs func on the cell
        # happy cases


        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(r, c, grid)
                    count += 1

        return count

#         Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# output: 1


        # edge cases
#         Input: grid = [
#   ["0","0","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

