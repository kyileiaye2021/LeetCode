class Solution:
    def bfs(self, heights, q, visited, dirs):
    # while pacific queue is not empty
        #   pop out the curr cell
        #   add it to pacific set
        #   go to the neighbors 
        #       if curr nei is within the bounds and higher than the curr cell 
        #           add it to the pacific queue

        while q:
            r, c = q.popleft()
            visited.add((r, c))

            for dx, dy in dirs:
                new_r = r + dx
                new_c = c + dy

                if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                    q.append((new_r, new_c))


    def dfs(self, heights, r, c, visited, directions):
        visited.add((r, c))
        
        for i, j in directions:
            new_r = r + i
            new_c = c + j

            if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                self.dfs(heights, new_r, new_c, visited, directions)

        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs
        # visit the curr cell
        # iterate thru its neighbor
        #   check if the curr neighbor is less than or equal to the curr cell and not visited
        #       call dfs on it


        # pacific cells
        # for pacific ocena
        # iterate thru the first row
        #   for each cell, if the cell is not visited, we will call dfs on it
        # iterate thru the first col
        #   for each cell, if the cell is not visited, we will call dfs on it

        # atlantic cells
        # for atlantic ocean
        # iterate thru the last row
        #   for each cell, if the cell is not visited, we will call dfs on it
        # iterate thru the last col
        #   for each cell, if the cell is not visited, we will call dfs on it

        # iterate thru one of the visited cells
        #     if the cell is already in the other set
        #           add it to the res list

        # return res list

        # rows = len(heights)
        # cols = len(heights[0])
        # pacific = set()
        # atlantic = set()
        # res = []

        # directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

        # # for pacific 
        # # first row
        # for c in range(cols):
        #     if (0, c) not in pacific:
        #         self.dfs(heights, 0, c, pacific, directions)

        # # first col
        # for r in range(rows):
        #     if (r, 0) not in pacific:
        #         self.dfs(heights, r, 0, pacific, directions)

        # # for atlantic
        # # last row
        # for c in range(cols):
        #     if (rows - 1, c) not in atlantic:
        #         self.dfs(heights, rows - 1, c, atlantic, directions)

        # # last col
        # for r in range(rows):
        #     if (r, cols - 1) not in atlantic:
        #         self.dfs(heights, r, cols - 1, atlantic, directions)
        
        # for (r, c) in pacific:
        #     if (r, c) in atlantic:
        #         res.append([r, c])

        # return res

        # BFS
        # pacific queue (first row cells and first col cells)
        # atlantic queue (last row cells and last col cells)
        # 4 dirs

        # pacific set

        # while pacific queue is not empty
        #   pop out the curr cell
        #   add it to pacific set
        #   go to the neighbors 
        #       if curr nei is within the bounds and higher than the curr cell 
        #           add it to the pacific queue

        # atlantic set

        # while atlantic queue is not empty
        #   pop out the curr cell
        #   add it to atlantic set
        #   go to the neighbors 
        #       if curr nei is within the bounds and higher than the curr cell 
        #           add it to the atlantic queue

        # find the common cells between atlantic and pacific set
        # return res

        res = []
        rows = len(heights)
        cols = len(heights[0])
        pacific_q = deque()
        atlantic_q = deque()
        pacific_set = set()
        atlantic_set = set()
        dirs = [[0,1], [1,0], [0, -1], [-1, 0]]

        # appending corresponding cells into pacific
        # first row
        for c in range(cols):
            pacific_q.append((0, c))

        # first col
        for r in range(rows):
            pacific_q.append((r, 0))

        self.bfs(heights, pacific_q, pacific_set, dirs)

        # appending corresponding cells into atlantic
        # last row
        for c in range(cols):
            atlantic_q.append((rows - 1, c))

        # last col
        for r in range(rows):
            atlantic_q.append((r, cols - 1))

        self.bfs(heights, atlantic_q, atlantic_set, dirs)

        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                res.append([r, c])

        return res
        





