class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = babd
        # output: bab

        # s = abcd
        # output: ''

        # s = "cbbd"
        # output: bb

        # s = "cbbc"
        # output: "cbbc"

        # s = ""
        # output: ""

        # iterate thru the chars
        # l and r at the curr char
        # max window = 0
        # max sub string = ""
        # until l and r ele are the same
        #   l -= 1
        #   r += 1
        # curr window size 
        # update the max window and keep track of curr substr if curr window > max window
        # return max sub str
        max_window = 0
        max_substr = ""

        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window = r - l + 1
                if curr_window > max_window:
                    max_window = curr_window
                    max_substr = s[l : r + 1]

                l -= 1
                r += 1

        for i in range(len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_window = r - l + 1
                if curr_window > max_window:
                    max_window = curr_window
                    max_substr = s[l : r + 1]
                l -= 1
                r += 1

        return max_substr



        