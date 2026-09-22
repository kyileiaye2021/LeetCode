class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        count = {}

        l = 0
        r = 0

        # bcbbbcba

        # aaa
        max_window = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                while count[s[r]] == 2:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        del count[s[l]]

                    l += 1

                count[s[r]] += 1

            curr = r - l + 1
            max_window = max(max_window, curr)
            r += 1

        return max_window

        