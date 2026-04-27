class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # creating tl, tr, bl, br
        # keep track of bl value
        # while br > 0
        #   iterate thru the row with br
        #       add br to bl
        #       decrement br by 1
        #       add tr to bl
        #       decrement tr by 1
        #       add tl to tr
        #       increment tl by 1
        #   decrement br by 1

        l = 0 
        r = len(matrix) - 1
        while l < r:
            t = l
            b = r

            # rotate starting from outside
            for i in range(r-l):
                topLeft = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]

                matrix[b - i][l] = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = topLeft
            
            l += 1
            r -= 1
