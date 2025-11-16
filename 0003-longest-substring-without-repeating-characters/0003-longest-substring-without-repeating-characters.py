class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # happy cases
        # s = "abcabcbb"
        # output: 3

        # s = "abcecce"
        # output: 4

        # edge cases
        # s = "mmmmm"
        # output: 1

        # s = "pkedng"
        # output: 6

        # slding window
        # l, r = 0
        # max len = 0
        # duplicate set 
        # iterate thru the s until r reaches the end
        #   if r ele is already visited
        #       until r ele is removed from the set
        #           remove the l ele from the set
        #           move l by 1
        #           
        #   add r ele to set
        #   keep track of curr window size and update the max len if needed
        #   move r by 1
        # return max len
        
        l, r = 0, 0
        longest = 0
        visited = set()

        while r < len(s):
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1

            visited.add(s[r])
            r += 1
            curr_window = r - l
            longest = max(longest, curr_window)

        return longest
        
        