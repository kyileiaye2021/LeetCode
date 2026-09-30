class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False # will determine the first row should be 0 or not

        # the first row and col will trace which row/col will be zero

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # setting zero in cols and rows according to first row and first col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

    
        # setting zero in first col if the first cell = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
            
        # setting zero in first row if rowZero = True
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        # itearte thru the matrix
        #   if curr matrix[i][j] == 0:
        #       curr[0][j]=0
        #       curr[i][0] = 0

        # iterate thru the first row (j) from second col
        #   if the curr [0][j] == 0
        #       iterate thru the row from second row [i]
        #           curr[i][j] = 0

        # iterate thru the first col(i) from second row
        #   if curr[i][0] == 0
        #       iterate thru the col from second col
        #           curr[i][j] = 0

        # if curr[0][0] == 0:
        #   iterate thru the first row and set val = 0
        #   iterate thru the second col and set val = 0
