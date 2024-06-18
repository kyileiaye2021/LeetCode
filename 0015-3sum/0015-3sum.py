class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #two pointer approach
        #sort the array first (key solution bc we want to use two pointer like in two sum - sorted array method)
        #create a list to store the sum lists
        #iterate over the list
            #if i > 0 and nums[i] == nums[i-1]
                #skip it (we only want distinct elements)
                
            #left pointer = curr_index + 1
            #right pointer = last index
        
            #loop until left != right
                #if nums[left] + nums[right] + curr_ele > 0
                    #update the right pointer
                # less than 0
                    #update the left pointer
                #if equal
                    #append the list
                    #update the pointers (because we don't return it so the loop doesn't get ended)
                    #In this case, we need to update only one pointer bc the other pointer will get updated in the above conditions
                    #so, update the left pointer
                    #if the left pointer is the same as prev left pointer, keep updating until it is not the same as prev left pointer (because we want distinct elements)
        #return the list
        
        nums.sort()
        result_lst = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            #two sum (sorted array) method starts here
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result_lst.append([nums[i], nums[left], nums[right]]) #we don't return anything here so the loop doesn't end
                    left += 1 #so, update the left pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result_lst
                        
                    
            
            
        
                    
       