class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # edge case
        # if every entry is '.', return true

        # row_set = {1: {}}
        # col_set = {2: {}}
        # square_set = {(0,0): {}}

        # iterate thru the rows:
        #   iterate thru the cols:
        #       if the entry is '.', continue
        #       temp row = row // 2
        #       temp col = col // 2
        #       check if the curr entry is already in the row set of ith row 
        #       or  the curr entry at jth col at that row is in the col set
        #       or the curr entry is already in the (temp row, temp col) in square_set
        #           return false
        #       add the curr entry to the row set at ith row
        #       add the curr entry to the col set at jth col
        #       add the curr entry to the (temp row, temp col) in the square set
        # return True

        rows = len(board)
        cols = len(board[0])

        # rows_set = {i: set() for i in range(rows)}
        # cols_set = {i: set() for i in range(cols)}
        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        square_set= defaultdict(set)
        print(square_set)

        for i in range(rows):

            for j in range(cols):
                if board[i][j] == '.':
                    continue

                temp_row = i // 3
                temp_col = j // 3
                if board[i][j] in rows_set[i] or board[i][j] in cols_set[j] or board[i][j] in square_set[(temp_row, temp_col)]:
                    return False

                rows_set[i].add(board[i][j])
                cols_set[j].add(board[i][j])
                square_set[(temp_row, temp_col)].add(board[i][j])

        return True