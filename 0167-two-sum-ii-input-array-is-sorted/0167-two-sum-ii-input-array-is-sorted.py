class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        As the list is sorted, we can take advantage of that. We can eliminate the right-pointered indexed var if the sum is greater than the target and the left-pointered indexed var if the sum is less than the target
        '''
        #two pointers approach
        #left pointer - first index
        #right pointer - last index
        #iterate until the left pointer is equal to the right pointer
            #add left indexed var and right indexed var
            #if it's greater than the target
                #move the right pointer to the left by 1
            #else if less than the target:
                #move the left pointer to the right by 1
            #else: ( equal to the target)
                #return the list of the left+1, right+1
                
                
        left = 0
        right = len(numbers) - 1
        while left != right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]
            
        