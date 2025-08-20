class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # aba 
        #  |
        # l, r will be expanded

        longest = 0
        longest_pan = ''

        for i in range(len(s)):
            
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > longest:
                    longest = curr_len
                    longest_pan = s[l:r+1]

                l -= 1
                r += 1

            # even len of s
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > longest:
                    longest = curr_len
                    longest_pan = s[l:r+1]

                l -= 1
                r += 1
        return longest_pan
            
            