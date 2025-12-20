class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # iterate thru the ele and keep track of the positions where the ele is 0
        # row set
        # col set

        # iterate thru the rows
        #   if the curr row is in row set
        #       iterate thru the cols
        #           make all col ele 0

        # iterate thru the col
        #   if the curr col is in col set
        #       iterate thru the row
        #           make all row ele 0

        row_set = set()
        col_set = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_set:
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if j in col_set:
                    matrix[i][j] = 0

        print(matrix)