class Solution:
    def dfs(self, board, r, c):
        if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != 'O':
            return

        board[r][c] = 'T'

        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs
        # if the cell is not on border and not visited
        # add the cells as visited
        # go to the neighbors and call dfs on nei

        # iterate thru the cells excluding the borders
        #   call dfs on the cells 

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    if board[r][c] == 'O':

                        self.dfs(board, r, c)

        print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

       