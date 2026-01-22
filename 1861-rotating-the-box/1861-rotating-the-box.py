class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        # create nxm 

        # itearte thru the cols
        #   iterate thru the rows from last  to first rows
        # inspect each col
        #   count '#' for each col
        #   mark the col that has block

        # inspect each col 
        #   if the col has block
        #       go until the block
        #   fill the '#' for corresponding count in each col


        m = len(boxGrid)
        n = len(boxGrid[0])
        res = [['.'] * m for _ in range(n)]


        for r in range(m):
            i = n - 1
            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][i], boxGrid[r][c] = boxGrid[r][c], boxGrid[r][i]
                    i -= 1

                elif boxGrid[r][c] == '*':
                    i = c - 1

        for c in range(n):
            for r in range(m - 1, -1, -1):
                res[c][m - 1 - r] = boxGrid[r][c]

        print(res)

        # res_rows = len(res)
        # res_cols = len(res[0])
        # obstacle_cols = {}
        # count = [0] * res_cols

        # for c in range(res_cols):
        #     for r in range(res_rows):
        #         if res[r][c] == '#':
        #             count[c] += 1

        #         elif res[r][c] == '*':
        #             if c in obstacle_cols:
        #                 obstacle_cols[c] += 1
        #             else:
        #                 obstacle_cols[c] = 1

        # for c in range(res_cols):
        #     r = res_rows - 1
        #     while r >= 0:
        #         if c in obstacle_cols:
        #             while obstacle_cols[c] > 0:
        #                 r -= 1
        #                 obstacle_cols[c] -= 1

        #             r -= 1

        #         for i in range(count[c]):
        #             res[r][c] = '#'
        #             r -= 1

        #         # empty the remaining ones
        #         res[r][c] = '.'
        #         r -= 1

        return res





                
        