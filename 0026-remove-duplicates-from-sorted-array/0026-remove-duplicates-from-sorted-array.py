class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #may not create a new list to store the elements
        #sort the array
        #create a var called unique_array_index to keep track of the array index
        #iterate over the ele in the list and check the current ele is equal to the prev ele
        #if it's not, assigned it to the current unique_array_index
        #update the current unique_array_index 

        nums.sort()

        #the list can be empty or only one element in the list
    
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        
        unique_array_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_array_index] = nums[i]
                unique_array_index += 1

        return unique_array_index
            
