class Solution:
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

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

        # for pacific 
        # first row
        for c in range(cols):
            if (0, c) not in pacific:
                self.dfs(heights, 0, c, pacific, directions)

        # first col
        for r in range(rows):
            if (r, 0) not in pacific:
                self.dfs(heights, r, 0, pacific, directions)

        # for atlantic
        # last row
        for c in range(cols):
            if (rows - 1, c) not in atlantic:
                self.dfs(heights, rows - 1, c, atlantic, directions)

        # last col
        for r in range(rows):
            if (r, cols - 1) not in atlantic:
                self.dfs(heights, r, cols - 1, atlantic, directions)
        
        for (r, c) in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res


