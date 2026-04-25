class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs
        visited = set()
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            image[r][c] = color

            for dir_r, dir_c in dir:
                new_r = dir_r + r
                new_c = dir_c + c

                if new_r in range(len(image)) and new_c in range(len(image[0])) and image[new_r][new_c] == orig_color:
                    dfs(new_r, new_c)
    
        dfs(sr, sc)
        return image


