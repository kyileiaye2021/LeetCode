class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # shortest path --> bfs
        # start from r - 0, c - 0
        # add it to queue along with 0 if the cell is 0
        # else return -1
        # last cell to keep track of the last visited cell
        # keep track of total_len
        # while queue
        #   pop out the curr r, c and len
        #   update total_len
        #   go to nei 
        #       check if nei is within bound, not visited, and 0
        #           add it to the queue with len + 1
        #           add it to visited
        #           update the last visited nei cell
        # return total_len if last visited cell is [last row][last col] else -1 

        queue = deque()
        dirs = [[0,1], [0,-1], [1,0], [-1,0], [-1,1], [1,-1], [-1,-1], [1,1]]
        visited = set()

        # starting from top left 
        if grid[0][0] != 0 or grid[len(grid) - 1][len(grid[0]) - 1] != 0:
            return -1
    
        if len(grid) == 1:
            return 1
        
        queue.append((0, 0, 1))
        visited.add((0, 0))
        while queue:
            curr_r, curr_c, curr_len = queue.popleft()

            if curr_r == len(grid) - 1 and curr_c == len(grid[0]) - 1:
                return curr_len
            # go to neighbors
            for dr, dc in dirs:
                new_r = curr_r + dr
                new_c = curr_c + dc

                if new_r in range(len(grid)) and new_c in range(len(grid)) and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    queue.append((new_r, new_c, curr_len + 1))
                    visited.add((new_r, new_c))

        
        return -1
                

            

            

        


        


