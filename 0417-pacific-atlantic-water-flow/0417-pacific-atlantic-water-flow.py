class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        dirs = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        # dfs
        def dfs(r, c, visited):
            visited.add((r,c))

            for dir_r, dir_c in dirs:
                new_r, new_c = r + dir_r, c + dir_c
                if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)


        rows = len(heights)
        cols = len(heights[0])

        # pacific ocean
        pacific = set()
        altantic = set()
        # first row
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, altantic)

        # first col
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, altantic)

        res = []
        for r, c in pacific:
            if (r, c) in altantic:
                res.append([r,c])

        return res


        