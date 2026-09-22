class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:


        # i =0, j = 0
        # ele = grid[0][0]
        # iterate thru ele with i
        #   iterate thru ele with j
        #       if j + k < n:
        #           j += 1
        #       elif j == n and i < m:
        #           i += 1
        #           j  = n - j
        #       elif j == n and i == m:
        #           i = 0
        #           j = 0
        #       temp = grid[i][j]
        #       grid[i][j] = ele
        #       ele = temp
        # return grid

        # first put all ele in 1d array
        # shifted idx = find the index where each ele will be assigned after shifting by k
        # find the index of 2d array where that ele will be assigned using shifted idx
        # assign the ele back to 2d arr

        m = len(grid)
        n = len(grid[0])

        k = k % (m * n)
        if k == 0:
            return grid

        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                idx = (i * n) + j # 1 d arr idx
                shifted_idx = (idx + k) % (m * n)

                # finding shifted idx in 2d arr
                i_idx = shifted_idx // n
                j_idx = shifted_idx % n

                res[i_idx][j_idx] = grid[i][j]

        return res

        
        