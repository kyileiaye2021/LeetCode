class Solution:
    def dfs(self, sr, sc, image, dirs, original, color):
        # change the color in the curr cell
        image[sr][sc] = color

        # go to the nei 
        #   check if they are in boundary and equal to original:
        #       call dfs on that 

        for dr, dc in dirs:
            new_r = dr + sr
            new_c = dc + sc

            if new_r in range(len(image)) and new_c in range(len(image[0])) and image[new_r][new_c] == original:
                self.dfs(new_r, new_c, image, dirs, original, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # dirs = 4 directions
        # call dfs on the start sr, sc
        # return matrix

        if image[sr][sc] == color:
            return image
        dirs = [[0,1], [0, -1], [1,0], [-1,0]]
        self.dfs(sr, sc, image, dirs, image[sr][sc], color)
        return image
        