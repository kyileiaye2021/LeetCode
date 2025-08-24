class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # go thru the cells
        #   if the fruit is rotten
        #       append it to the queue
        #   if the fruit is fresh
        #       increment the fresh

        queue = deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minute = 0
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, minute))

                if grid[r][c] == 1:
                    fresh += 1

        while queue:
            curr_r, curr_c, curr_min = queue.popleft()
            minute = curr_min

            for dx, dy in dirs:
                new_r, new_c, new_min = curr_r + dx, curr_c + dy, curr_min + 1
                if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c, new_min))

        return -1 if fresh > 0 else minute

        





        

