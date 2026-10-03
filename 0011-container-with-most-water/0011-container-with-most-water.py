class Solution:
    def maxArea(self, height: list[int]) -> int:
        # happy cases
        # [2,4,2,3,8,4]
        # 16

        # edge cases
        # [1,1,1,1] 
        # 3

        # [1, 1]
        # 1

        # [0, 1, 5, 0]
        # 1

        # nested for loop - O(n^2)
        # 2 pointer 
        
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            hei = min(height[l], height[r])
            leng = r - l 
            area = hei * leng
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

