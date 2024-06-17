class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Method 1
        #sort the list first
        #iterate over the list 
        #check the current element is equal to prev element
        #if it's, return true
        #if it's not, return false

        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        '''
        #Method 2
        #create a hashset 
        #iterate over the list 
        #check if the current ele is already in the set
        #if it's, return true
        #if it's not, add current ele in the set
        #if no duplicates in the list, false

        hashset = set()
        for ele in nums:
            if ele in hashset:
                return True
            hashset.add(ele)

        return False

        