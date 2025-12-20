class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l = 0
        r = len(matrix[0])
        t = 0
        b = len(matrix)

        res = []

        while l < r and t < b:

            # go from left to right
            for j in range(l, r):
                res.append(matrix[t][j])
            t += 1

            # go from top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not(l < r and t < b):
                break

            # go from right to left
            for j in range(r-1, l -1, -1):
                res.append(matrix[b - 1][j])
            b -= 1

            # go from bottom to top
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            

        return res

