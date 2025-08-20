class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max area = 0
        # l and r pointer
        # l = 0, r = end of the list
        # until l reach r
        #   find the diff of l and r
        #   get the min of l and r pointer ele 
        #   find the area and update the max area
        # return max area

        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            diff = r - l
            curr_area = min(height[l], height[r]) * diff
            max_area = max(max_area, curr_area)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area