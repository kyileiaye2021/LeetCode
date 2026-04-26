class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substr = ""
        max_window = 0
        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
    
                cur_window = r - l + 1
                if cur_window > max_window:
                    max_substr = s[l:r + 1]
                    max_window = cur_window
            
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_window = r - l + 1
                if cur_window > max_window:
                    max_substr = s[l:r + 1]
                    max_window = cur_window

                l -= 1
                r += 1
        
        return max_substr

    