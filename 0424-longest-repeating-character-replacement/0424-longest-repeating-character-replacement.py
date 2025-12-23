class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # happy case
        # s = "ABAB", k = 2
        # 4

        # s = "BFRGG", k = 2
        # output: 4

        # s = "AAAAA", k = 1
        # output: 5

        # s = "khgtno", k = 3
        # output: 4

        # s = "t", k = 1
        # output: 1

        # s = "sty", k = 0
        # output: 1

        # s = "sssty", k = 0
        # output: 3

        # sliding window
        # l = 0, r = 0
        # hashmap to keep track of the freq of chars in the window
        # iterate thru the s until r reaches the end
        #   add the curr ele to the hashmap
        #   check if window size - the most freq ele num == k:
        #       update the window size
        #   while window size - the most freq ele num >= k:
        #       shrink the window by decrementing l pointer ele freq num
        #       increment l pointer
        # increment r
        # return max window size

        l = 0
        r = 0
        map = {}
        max_window = 0
        while r < len(s):
            map[s[r]] = map.get(s[r], 0) + 1
            most_freq_ele_count = max(map.values())
            curr_window = r - l + 1

            if curr_window - most_freq_ele_count <= k:
                max_window = max(curr_window, max_window)

            while curr_window - most_freq_ele_count > k:
                map[s[l]] -= 1
                l += 1
                curr_window = r - l + 1
                most_freq_ele_count = max(map.values())

            r += 1
        
        return max_window

