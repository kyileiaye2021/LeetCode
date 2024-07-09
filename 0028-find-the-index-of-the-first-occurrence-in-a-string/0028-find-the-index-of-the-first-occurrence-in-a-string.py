class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #Assumption 
        # both str will have lowercase chars
        # both str cannot be empty
        
        # High level Plan
        # Two pointer technique
        # * create two pointers left and right
        # * whenever we find the first char of needle in haystack, mark that char's
        #   index. and check other char by shifting the right pointer
        
        # Low Level Plan
        # * create two pointers left and right first pointing to index 0 and 0 of                 haystack
        # * iterate over the list until left pointer reaches the end
        
        #   * if the right char is pointing to the var equal to the index var in                   needle
        #       * shift right by 1
        #       * shift curr pointer to right by 1 in needle
        #.      * if the curr pointer in needle == the len of the needle
        #           * return left
        #   * shift left to the var that right is currently pointing to
        #   * reset index to 0
        # * return -1 
        if len(needle) > len(haystack):
            return -1
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return i
            
        return -1
                
                