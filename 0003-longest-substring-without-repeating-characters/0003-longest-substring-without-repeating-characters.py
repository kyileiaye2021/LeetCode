class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: nested for loop O(n^2)
        # sliding window
        # set to maintain the unique ele
        # i, j pointers
        # max window
        # while j is < len(s)
        #   while the curr ele is in the set
        #       remove the i ele 
        #   
        #   add it to the set
        #   increment j by 1
        #   update the curr window size
        #   update the max window size

        unique = set()
        i, j = 0, 0
        max_window = 0
        curr_window = 0

        while j < len(s):
            while s[j] in unique:
                unique.remove(s[i])
                i += 1

            unique.add(s[j])
            j += 1
            curr_window = j - i
            max_window = max(max_window, curr_window)
            
        return max_window        