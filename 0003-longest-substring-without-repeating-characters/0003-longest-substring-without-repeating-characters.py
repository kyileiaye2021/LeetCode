class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window 2 pointers
        # set in window to check duplicates

        # l , r

        l = 0
        visited = set()
        max_window = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])
            cur_window = r - l + 1
            max_window = max(cur_window, max_window)

        return max_window
                
            


        