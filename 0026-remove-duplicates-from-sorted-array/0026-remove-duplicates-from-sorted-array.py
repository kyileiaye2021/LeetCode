class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
    # Happy cases
    # input - [1,1,2]
    # output - 2
    
    # Edge cases
    # input - []
    # output - 0
    
    # input - [1]
    # output - 1
    
    # Two pointer approach
    # if len(nums) == 0:
    #   return []
    # p and q initialize to 1,1
    # p pointing to the ele and iterate over the ele in the list
    # q point to index of the unique ele 
    # while p reaches the end of the list
    #   check if the curr p element is not the same as the prev ele
    #       assign p ele into the positon that q pointer currently points to
    #       increment q by 1
    #   increment p by 1
    # return q
    
    # Time complexity - O(n)
    # Space complexity - O(1)
    
        if len(nums) == 0:
            return []

        p, q = 1 , 1

        while p < len(nums):

            if nums[p] != nums[p - 1]:
                nums[q] = nums[p]
                q += 1

            p += 1

        return q

