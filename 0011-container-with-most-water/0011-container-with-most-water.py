class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Happy cases
        # input - height = [1,2,3]
        # output - 2
        
        # Edge cases
        # input - height = [1, 1]
        # output - 1
        # input - height = [0, 0]
        # output - 0
        # input - height = [1]
        # output - 0
        
        # Edge cases
        # find the area of the container
        # area = height * width
        # width --difference between ele 
        
        # Two pointer approach
        # create 2 pointers p, q
        # create a var to trace the max area
        # iterate over the list until p passes q    
        #   find the diff between p and q 
        #   find the min height between p ele and q ele
        #   find the curr area 
        #   update the max area if curr area is greater than max area
        #   check if the p ele is greater than q ele
        #       decrement q by 1
        #   else:
        #       increment p by 1
        # return the max area
        
        # Time complexity - O(n)
        # Space complexity - O(1)
        
        p = 0
        q = len(height) - 1
        
        max_area = 0
        
        while p < q:
            diff = q - p
            ht = min(height[p], height[q])
            curr_area = diff * ht
            max_area = max(max_area, curr_area)
            
            if height[p] > height[q]:
                q -= 1
            else:
                p += 1
                
        return max_area