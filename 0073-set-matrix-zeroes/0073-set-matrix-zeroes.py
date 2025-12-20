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

        # row_set = set()
        # col_set = set()

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             row_set.add(i)
        #             col_set.add(j)

        # for i in row_set:
        #     for j in range(len(matrix[0])):
        #         matrix[i][j] = 0
        
        # for j in col_set:
        #     for i in range(len(matrix)):
        #         matrix[i][j] = 0

        # print(matrix)

        # set the flags for first row and first col
        first_row_flag = True
        first_col_flag = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_flag = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_flag = False
 
        # mark which rows and cols marked to be 0 in first row and col
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # mark all rows and cols as 0 if they need to be 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
 
        # mark the first row and first col as 0 if they need to be 0
        if not first_row_flag:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if not first_col_flag:
            for i in range(len(matrix)):
                matrix[i][0] = 0