class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # restrictions
        # the visited cell should be within boundary
        # the visited cell should be '.'
        # for the exit:
        # the visited cell should be at the border and not the same as entrance

        #BFS
        # input: [['+', '+', '+']
        #          *, '.', '.'
        #          ['+', '+', '+]]
        # output - 2

        # input: [[*, '+']]
        # output: -1


        rows, cols = len(maze), len(maze[0])
        entrance_r, entrance_c = entrance[0], entrance[1]
        # empty = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if maze[r][c] == '.' and (r, c) != (entrance_r, entrance_c):
        #             empty += 1

        # print(f"empty1: {empty}")
        # if empty == 0:
        #     return -1


        count = 0
        queue = collections.deque()
        queue.append((entrance_r, entrance_c, count))
        maze[entrance_r][entrance_c] = '+'

        dir = [[0,1], [0,-1], [1,0], [-1, 0]]

        while queue:

            queue_len = len(queue)

            # for _ in range(queue_len):

            curr_r, curr_c, curr_count = queue.popleft()
            if (curr_r == 0 or curr_r == rows - 1 or curr_c == 0 or curr_c == cols - 1) and [curr_r, curr_c] != entrance:
                return curr_count

            for dx, dy in dir:
                new_r, new_c = curr_r + dx, curr_c + dy

                if new_r in range(rows) and new_c in range(cols) and maze[new_r][new_c] == '.':
                    maze[new_r][new_c] = '+'
                    # empty -= 1
                    queue.append((new_r, new_c, curr_count + 1))

        return -1




