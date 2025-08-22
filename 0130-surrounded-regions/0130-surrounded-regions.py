class Solution:
    def dfs(self, board, r, c):
        board[r][c] = 'T'
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dx, dy in dirs:
            new_r = r + dx
            new_c = c + dy

            if new_r in range(len(board)) and new_c in range(len(board[0])) and board[new_r][new_c] == 'O':
                self.dfs(board, new_r, new_c)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs 
        #   mark the cell as 'x'
        #   go to neighbor
        #   if each neighbor is within the bound - 1 and not visited and '0
        #       call dfs on the neighbor cell
        # 
        # iterate thru every cell
        #   check if the cell is '0' and not visisted
        #       call dfs on the cell

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1): # we changed O to T at the border or border connected cells
                    self.dfs(board, r, c)

        print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                    
        print(board)