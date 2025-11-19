class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # create a matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.m = [[0] * cols for _ in range(rows)]

        # iterate thru each row
        #   first col stay the same
        #   accumulate the sum up in each col of ith row
        for r in range(rows):
            self.m[r][0] = matrix[r][0]
            for c in range(1, cols):
                self.m[r][c] += self.m[r][c - 1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # iterate thru from the row1 to row2 inclusive
        #   if col is > 0
        #       diff = subtract the col2 ele - col1 - 1 ele in ith row
        #       add the diff to the res
        #   else
        #       add the col2 ele to the res
        #       
        res = 0
        for r in range(row1, row2 + 1):
            if col1 > 0:
                diff = self.m[r][col2] - self.m[r][col1 - 1]

            else:
                diff = self.m[r][col2] 
            res += diff

        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)