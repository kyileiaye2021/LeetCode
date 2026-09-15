class Solution:
    def isPalindrome(self, s: str) -> bool:

        # ignore whitespaces and non-alphanumeric 
        # if 2 pointers is non-alphanumeric chars, move that pointer

        # if 2 pinter ele == the same
        # move both pointers inwards
        # stop when l and r are =

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            
            else:
                return False

        return True

            
        