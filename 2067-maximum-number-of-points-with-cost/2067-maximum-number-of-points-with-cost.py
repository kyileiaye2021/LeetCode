class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # dp

        # iterate thru the matrix from the second row
        #   create left and right pointer of the row size
        #
        #   left arr
        #   iterate thru the curr_row - 1 from index 1
        #       curr-val = max(points[curr_row - 1][i], points[curr_row - 1][i-1] -1)
        #       assign curr_val to the left[curr_row][i]

        #   right arr
        #   iterate thru the curr_row -1 from second last index
        #       curr_val = max(points[curr_row - 1][i], points[curr_row-1][i+1] - 1)
        #       assign curr_val to the right[curr_row][i]

        # iterate thru the cols 
        #   get the max of curr ith value of left and right
        #   add it to the curr val 

        # return the max value in the last row

        rows = len(points)
        cols = len(points[0])

        for r in range(1, rows):
            left = [0] * cols
            right = [0] * cols
            
            # left arr
            left[0] = points[r - 1][0]
            for c in range(1, cols):
                curr_max = max(points[r - 1][c], left[c - 1] - 1)
                left[c] = curr_max

            # right arr
            right[cols - 1] = points[r - 1][cols - 1]
            for c in range(cols - 2, -1, -1):
                curr_max = max(points[r - 1][c], right[c + 1] - 1)
                right[c] = curr_max
            
            # updating the curr row values 
            for c in range(cols):
                points[r][c] = max(left[c], right[c]) + points[r][c]

        return max(points[rows - 1])


            




        