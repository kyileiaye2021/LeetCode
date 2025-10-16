class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # set to store the rows and cols to make zeros
        # iterate thru the rows and cols
        # spot the zeros in each col and row
        # if 0 is found
        #   store the row and col into the set

        # iterate thru the row set
        #   iterate thru the cols in the row
        #       make them all 0

        # iterate thru the col set
        #   iterate thru the rows in the col
        #       make them all 0

        row_set = set()
        col_set = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)

        for r in row_set:
            for c in range(cols):
                matrix[r][c] = 0

        for c in col_set:
            for r in range(rows):
                matrix[r][c] = 0

            
 
