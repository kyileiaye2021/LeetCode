class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Assumption
        # the res is a substring with no unique character
        
        # Low Level Plan
        # *Two pointer technique
        #   * the left pointer will point to the first index
        #   * create a dict to store the curr char and its frequency
        #   * the right pointer traverse the whole string
        #       * if it's not in the dict
        #           * add the curr char to the dict
        #           * shift the right pointer
        #       *else: shift left to where the right pointer curr points to
        #       * move the right pointer
        #       * reset the new dict
        
        
        left = 0
        right = 0
        check_duplicates = set()
        longest_length = 0
        
        for right in range(len(s)):
            while s[right] in check_duplicates:
                check_duplicates.remove(s[left]) # shrink the window
                left += 1 
            
            check_duplicates.add(s[right])
            longest_length = max(longest_length, right - left + 1)
            
        return longest_length
                
    