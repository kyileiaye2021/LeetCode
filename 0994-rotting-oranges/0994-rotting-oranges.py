class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # bfs
        # add all rotten oranges in the queue
        # pop out and go to nei oranges
        # update the min time
        # check if there are still fresh oranges
        #   return -1
        # else return min time

        time = 0
        queue = deque()
        fresh = 0
        dir = [[0,1], [0, -1], [1, 0], [-1, 0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, time))
                
                if grid[r][c] == 1:
                    fresh += 1

        
        while queue:
            r, c, time = queue.popleft()

            for dir_r, dir_c in dir:
                new_r = r + dir_r
                new_c = c + dir_c

                if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    fresh -= 1

                    queue.append((new_r, new_c, time + 1))
            
        return time if fresh == 0 else -1








        