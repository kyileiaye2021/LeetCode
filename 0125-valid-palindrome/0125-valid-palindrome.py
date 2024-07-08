class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer approach
        # * create left and right pointers
        # * iterate over the str unitl left pointer passes right one
        #   * check if the left is not equal to right
        #       * check if the left is non-alphanumeric
        #           * shift left by 1 to right
        #       * check if the right is non-alphanumeric
        #           * shift right by 1 to left
        #       * check if the right and left are both non_alphanumeric
        #           * shift right and left by 1
        #       * if both left and right are alphanumeric
        #           *return False
        #   * otherwise: shift both left and right by 1
        
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                if s[left].isalnum() and s[right].isalnum():
                    return False
                elif not s[left].isalnum() and s[right].isalnum():
                    left += 1
                elif not s[right].isalnum() and s[left].isalnum():
                    right -= 1
                else:
                    right -= 1
                    left += 1
            else:
                right -= 1
                left += 1
                
        return True

                