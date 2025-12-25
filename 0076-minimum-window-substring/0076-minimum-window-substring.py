class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap for t and curr window in s
        # l,r
        # hashmap for t 
        # min window size = largest ele
        # min window substring = ""
        # have and need
        # while r < len(s)
        #   check if the curr char in t hashmap
        #       add the curr char in s hashmap
        #       if curr char freq in t == that in s
        #           increment the have
        #   while have == need
        #       curr window size 
        #       curr window substr
        #       if curr window size < min window 
        #           update min window size and min window substring
        #       check if l pointer ele in s hashmap
        #           decrement that freq 
        #           if s hashmap freq < t hashmap freq
        #               have -= 1
        #       l += 1
        #   r += 1
        # return min window substring

        l = 0
        r = 0
        min_window_size = float('inf')
        min_window_substr = ""
        have = 0
        t_hashmap = Counter(t)
        need = len(t_hashmap)
        s_hashmap = {}

        while r < len(s):
            if s[r] in t_hashmap:
                s_hashmap[s[r]] = s_hashmap.get(s[r], 0) + 1
                if t_hashmap[s[r]] == s_hashmap[s[r]]:
                    have += 1

            while have == need:
                curr_window_size = r - l + 1
                if curr_window_size < min_window_size:
                    min_window_size = curr_window_size
                    min_window_substr = s[l : r + 1]
                
                # removing l char
                if s[l] in s_hashmap:
                    s_hashmap[s[l]] -= 1
                    if s_hashmap[s[l]] < t_hashmap[s[l]]:
                        have -= 1

                l += 1

            r += 1

        return  min_window_substr




