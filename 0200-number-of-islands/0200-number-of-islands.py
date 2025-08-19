class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # dfs func  (grid, r, c)
        #   mark the curr cell as visited
        #   for each neighbor of the curr cell
        #       check if they are within the boundary and they are not visited
        #           check if they are 1
        #               call dfs on those cells
        # 
        # count = 0
        # num of r, c 
        # visited set to check the visited vertices
        # iterate thru each cell
        #   check if the curr cell is not visited and the curr cell is 1
        #       call dfs func
        #       increment the count 
        # return count 
        
        def dfs(r, c):
            # base case
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
                
            grid[r][c] = '0'
            
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
    
    
        count = 0
        rows = len(grid)
        cols = len(grid[0])    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
                
        return count
        
            