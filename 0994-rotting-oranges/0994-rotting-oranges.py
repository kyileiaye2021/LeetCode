class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # layer
        # bfs 

        # edge cases
        # 0 | 0 | 0
        # 0 | 0 | 0
        # 0

        # 1 | 1 | 1
        # 1 | 1 | 1
        # -1

        # 2 | 2 | 2
        # 2 | 2 | 2
        # 0

        # dq 
        # fresh = 0
        # add rotten oranges in dq (cells, min = 0)
        # increment fresh
        # while dq
        # pop the rotten out
        # total time = time
        # new time = time + 1
        # go to 4 dir
        #   check if nei within bound and fresh
        #   make them to 2
        #   add them to dq
        # return time if fresh == 0 else - 1

        dq = deque()
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    dq.append((i, j, 0))

        total_time = 0
        while dq:
            i, j, time = dq.popleft()
            total_time = time
            new_time = time + 1

            for dx, dy in dir:
                new_x, new_y = dx + i, dy + j

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                    fresh -= 1
                    grid[new_x][new_y] = 2
                    dq.append((new_x, new_y, new_time))
        
        return total_time if fresh == 0 else -1




