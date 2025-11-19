class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # create a matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.m = [[0] * (cols + 1) for _ in range(rows + 1)]

        # 1D PREFIX SUM SOLUTIOIN
        # # iterate thru each row
        # #   first col stay the same
        # #   accumulate the sum up in each col of ith row
        # for r in range(rows):
        #     self.m[r][0] = matrix[r][0]
        #     for c in range(1, cols):
        #         self.m[r][c] += self.m[r][c - 1] + matrix[r][c]

        # 2D PREFIX SUM SOLUTION
        # iterate thru the rows
        #   prefix = 0
        #   iterate thru the cols
        #       accumulate the prefix by adding the curr matrix [r][c]
        #       above
        #       assign the prefix + above to m[r + 1][c + 1]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.m[r][c+1]
                self.m[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # 1D PREFIX SUM SOLUTION   
        # iterate thru from the row1 to row2 inclusive
        #   if col is > 0
        #       diff = subtract the col2 ele - col1 - 1 ele in ith row
        #       add the diff to the res
        #   else
        #       add the col2 ele to the res
        #  

        # res = 0
        # for r in range(row1, row2 + 1):
        #     if col1 > 0:
        #         diff = self.m[r][col2] - self.m[r][col1 - 1]

        #     else:
        #         diff = self.m[r][col2] 
        #     res += diff

        # return res

        # 2D PREFIX SUM SOLUTION 
        # change row 1 to row1 + 1, ...
        # bottomRight = entry at row2 col2
        # top = entry at row1 - 1 col2
        # left = entry at row2 col1-1
        # top_left = entry at row1-1 col1-1 (subtracted twice so add it again)
        # bottomRight - top - left + top_left

        row1 = row1 + 1
        row2 = row2 + 1
        col1 = col1 + 1
        col2 = col2 + 1

        bottomRight = self.m[row2][col2]
        top = self.m[row1 - 1][col2]
        left = self.m[row2][col1 - 1]
        topleft = self.m[row1 - 1][col1 - 1]

        return bottomRight - top - left + topleft
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)