class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Since there would be 3 unique elements in the list, we can use two pointers pointing to the first index and last index.
        We may not increment i by 1 if the right pointer moves to the left by 1 because the list will not be sorted well 
        '''
        
        #0's must be at the beginning and 2's must be at the end of the list 
        
        #Two pointer approach (based on quick sort but optimized version)
        #create two pointers
        
        #iterate through the list until the curr index passes the right pointer
            #if curr ele == 0:
                #swap the curr ele with the one that left pointer currently points to 
                #increment the left pointer by 1
            #elif curr ele == 2:
                #swap curr ele with the one that right poiinter currently points to
                #decrement the right pointer by 1
                #decrement i (current index) by 1
            #increment i by 1
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        l, r = 0, len(nums) - 1 
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1
        
                