class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # count the num of rotten fruits
        # create a queue
        # fresh = 0
        # iterate thru the grid 
        #   update the fresh
        #   put the rotten fruit into the queue
        # until the queue is empty
        #   length of queue
        #   iterate thru the len of queue
        #       pop out the curr rotten fruit
        #       for each neighbor
        #           make the curr neighbor as rotten
        #           put the curr neighbor to the queue
        #   increment time elapsed

        # CAREFUL: IF THE LAST ROTTEN FRIUT IS POP OUT AND NO FRESH IS LEFT THEN THE TIME ELAPSED IS STILL INCREMENTED. SO, WE HAVE TO CHECK IF THE FRESH IS LEFT OR NOT.
        queue = deque()
        fresh = 0
        time_elapsed = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        while queue and fresh > 0:
            queue_len = len(queue)

            for _ in range(queue_len):
                curr_r, curr_c = queue.popleft()

                for dir_r, dir_c in directions:
                    new_r = dir_r + curr_r
                    new_c = dir_c + curr_c

                    if new_r in range(0, rows) and new_c in range(0, cols) and grid[new_r][new_c] == 1:
                        fresh -= 1
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 2

            time_elapsed += 1

        return time_elapsed if fresh == 0 else -1





                