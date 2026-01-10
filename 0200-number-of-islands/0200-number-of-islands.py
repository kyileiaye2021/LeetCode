class Solution:
    def dfs(self, grid, r, c, visited, dirs):
        visited.add((r, c))

        for dx, dy in dirs:
            new_r = r + dx
            new_c = c + dy

            if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                self.dfs(grid, new_r, new_c, visited, dirs)


    def bfs(self, grid, r, c, visited, dirs):
        visited.add((r, c))
        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.pop()
            for dx, dy in dirs:
                new_r = r + dx
                new_c = c + dy

                if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))

    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # mark the curr cell as visited
        # go to 4 directions from the curr cell
        #   if it's not visited and 1
        #       call dfs on that cell

        # iterate thru the rows 
        #   iterate thru the cols
        #       if the curr cell is 1 and not visited
        #           call dfs 
        #           increment group count
        # return group count

        # group = 0
        # rows = len(grid)
        # cols = len(grid[0])
        # visited = set()
        # dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) not in visited and grid[r][c] == '1':
        #             self.dfs(grid, r, c, visited, dirs)
        #             group += 1

        # return group

        # time = O(m * n)
        # space = O(m * n)


        # -----------------------------------------------------

        # BFS
        group = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    self.bfs(grid, r, c, visited, dirs)
                    group += 1
        return group
        