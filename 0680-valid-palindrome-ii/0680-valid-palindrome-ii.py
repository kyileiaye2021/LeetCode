class Solution:
    def validPalindrome(self, s: str) -> bool:
        # happy case
        # s = "aba"
        # output = true

        # edge case

        # s = "ab"
        # output = true

        # s = "abcgdba"
        # output = false

         # s = "abca"
        # output = true

        # two pointer 

        return_val = True
        l, r = 0, len(s) - 1

        while l < r:
    
            if s[l] != s[r] :

                return_val_l = self.valid(s, l + 1,r)
                return_val_r = self.valid(s, l, r-1)
                return return_val_l or return_val_r

            else:
                l += 1
                r -= 1

        return True

    def valid(self,s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True