class Solution:
    def dfs(self, r, c, visited, heights, dir):
            
        visited.add((r, c))

        for dx, dy in dir:
            new_r = r + dx
            new_c = c + dy

            if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r,new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                self.dfs(new_r, new_c,visited, heights, dir)
            

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from edges 
        # mark the cell as visited
        # go to the neighbors
        #   if the neighbor is within the bound and the neighbor is greater than or == curr cell
        #       add the neighbor cell to the corresponding ocean

        # Pacific
        # visited_pacific
        # iterate thru the ele in the 1st row
        #   if the curr cell not visited
        #       call dfs on curr cell
        # iterate thru the rows in 1st col
        #   if the curr cell not visited
        #       call dfs on curr cell

        # atlantic 
        # visited_atlantic
        # itereate thru the ele in the last row
        #   if curr cell not visited
        #       call dfs on curr cell
        # iterate thru the ele in the last col
        #   if curr cell not visited
        #       call dfs on curr cell 

        # res list
        # iterate thru the pacific set 
        #   check if the curr cell is also in atlantic 
        #       add it to res

        # return res

        rows = len(heights)
        cols = len(heights[0])
        dir = [[0,1], [0,-1], [1,0], [-1,0]]

        # pacific ocean
        visited_p = set()
        visited_a = set()
        for c in range(cols):
            if (0,c) not in visited_p:
                self.dfs(0, c, visited_p, heights, dir) # pacific

            if (rows - 1, c) not in visited_a:
                self.dfs(rows - 1, c, visited_a, heights, dir) # atlantic


        for r in range(rows):
            if (r, 0) not in visited_p:
                self.dfs(r, 0, visited_p, heights, dir) # pacific

            if (r, cols - 1) not in visited_a:
                self.dfs(r, cols - 1, visited_a, heights, dir) # atlantic

        res = []
        for (r, c) in visited_p:
            if (r, c) in visited_a:
                res.append([r,c])

        return res
