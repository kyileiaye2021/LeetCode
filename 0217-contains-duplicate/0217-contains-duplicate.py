class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Happy cases
        # input - [1,2,3,1]
        # output - true
        
        # input - [1,1,3,4,3,2,4,1]
        # output - true
        
        # Edge cases
        # input - []
        # output - false
        # input - [2]
        # output - false
        
        # dictionary approach
        # create a dict
        # iterate over the list
        #   check if the ele is in the dict
        #       increment the ele by 1
        #   set the ele in the dict with the val of 1
        # iterate over the dict
        #   check if the ele in the dict has more than 1 freq
        #       return true 
        # return false
        
        freq = {}
        for ele in nums:
            if ele not in freq:
                freq[ele] = 1
            else:
                freq[ele] +=1
                
        for key, value in freq.items():
            if value > 1:
                return True
            
        return False