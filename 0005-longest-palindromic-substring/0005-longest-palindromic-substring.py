class Solution:
    def longestPalindrome(self, s: str) -> str:

        # the word is not fully panlindrome
        # we have to find the longest substr that is panlindrome 

        # iterate thru each char in the word

        #   # for odd len 
        #   start from curr i (l, r pointers)
        #   while l and r are the same
        #       move l by 1 to left
        #       move r by 1 to right
        #   create the curr substr
        #   check if the substr len is > the longest
        #       update the longest substr with curr substr
        #       update the longest len with curr len
        
        #   for even len
        #   start l at curr
        #   start r at i + 1
        #   while l and r are the same
        #       move l by 1 to left
        #       move r by 1 to right
        #   create the curr substr
        #   check if the substr len is > the longest
        #       update the longest substr with curr substr
        #       update the longest len with curr len
        longest = 0
        longest_substr = ""

        for i in range(len(s)):
            # for odd len
            l = i 
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            curr_substr = s[l + 1: r]
            if len(curr_substr) > longest:
                longest_substr = curr_substr
                longest = len(curr_substr)


            # for even len
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            curr_substr = s[l + 1: r]
            if len(curr_substr) > longest:
                longest_substr = curr_substr
                longest = len(curr_substr)
        return longest_substr


        