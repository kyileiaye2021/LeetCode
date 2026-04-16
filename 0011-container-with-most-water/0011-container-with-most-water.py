class Solution:
    def maxArea(self, height: List[int]) -> int:

        # happy cases
        # [1,8,6,2,5,4,8,3,7]
        # 49

        # [1,1]
        # 1

        # [1,0,1]
        # 2

        # [0,0]
        # 0

        # [0, 1, 0]
        # 0

        # [1,1,1]
        # 1

        # brute force - O(n^2)
        # two pointers - 
        # l and r 
        # calculate the area
        
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] > height[r]:
                r -= 1

            else:
                l += 1

            
        return max_area

            




        
        