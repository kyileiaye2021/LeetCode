class Solution:
    def maxArea(self, height: List[int]) -> int:

        # two pointers
        # iterate thru the ele until two pointers cross each other
        #   get the len
        #   get the lower height
        #   calculate the area
        #   update the max area if needed
        #   move the lower height bar
        # return max area

        # [2,1,3]
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            x = r - l
            y = min(height[l], height[r])
            area = x * y
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


        