class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace least frequent ele in the window
        # hashmap
        # l, r
        # max window size = 0
        # while r < len(s)
        # add the curr ele to hashmap
        # get the most freq count
        # while curr window size - most freq count > k
        #   decrement l ele count in hashmap
        #   increment l by 1
        # keep track of the max window size
        # increment r by 1
        # return max window size

        l = 0
        r = 0
        count = {}
        max_window_size = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            max_window_size = max(max_window_size, (r - l + 1))
            r += 1

        return max_window_size

