class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # creating a set to store the ele in order
        # create longest seq length to 0
        
        # iterate over the nums
        #   * check if the num-1 is not in set
        #   * curr num will be start num
        #   * if there are right neighbor (num + 1) 
        #       * update the curr length
        #   * update the longest seq length
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            
            if (n - 1) not in numSet: #if there is no left neighbor, n is the start num
                length = 0 #to keep track of the length of curr seq
                
                while (n + length) in numSet: #calculate the length of seq
                    length += 1
            
                longest = max(longest, length)
                
        return longest