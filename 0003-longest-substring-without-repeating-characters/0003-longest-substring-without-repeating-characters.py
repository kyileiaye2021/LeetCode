class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # l, r = 0
        # set
        # iterate the s with r 
        #   if the curr ele not in set
        #       add it to set and increment r
        #   else
        #       update the max window if needed
        #       remove the l ele until the curr ele is in the set
        # return the max window
        l = 0
        r = 0
        unique = set()
        max_window = 0
        while r < len(s):
            
            if s[r] in unique:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1

            unique.add(s[r])
            max_window = max(max_window, r - l + 1)
            r += 1

        return max_window

        
        