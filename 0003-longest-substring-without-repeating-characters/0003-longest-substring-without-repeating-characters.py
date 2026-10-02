class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # happy cases
        # 'abcabc', 3

        # 'abba', 2

        # 'abc', 3

        # edge cases
        # 'bbbb', 1

        # '', 0

        # 'kle8 9', 6

        # sliding window
        # O(n) time
        # O(n) space

        visited = set()
        max_window = 0
        l = r = 0
        while r < len(s):

            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            
            visited.add(s[r])
            cur_window = r - l + 1
            max_window = max(max_window, cur_window)
            r += 1

        return max_window

        


