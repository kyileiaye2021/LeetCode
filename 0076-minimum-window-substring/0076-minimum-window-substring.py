class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # hashmap for t and one for s
        # len of t hashmap  =>. need
        # min_window = inf
        # l, r
        # check = 0

        # while r is within the bound
        #   while check is equal to need
        #       curr window = r - l + 1
        #       update min window
        #       decrement the freq of l ele in s hashmap
        #       if l ele freq is 0, remove from s hashmap
        #       decrement the check
        #       move l by 1

        #   add the r ele to s hashmap
        #   if r ele in t hashmap and t[r ele ] is the same as the s[r ele]
        #       increment check by 1
        #   r += 1
        t_map = Counter(t)
        print(t_map)
        need = len(t_map)
        min_len = float('inf')
        min_window = ""
        l, r = 0, 0
        check = 0
        s_map = {}

        while r < len(s):


            s_map[s[r]] = s_map.get(s[r], 0) + 1
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                check += 1
            r += 1
            while check == need:
                curr_window = r - l

                print(curr_window)
                if curr_window < min_len:
                    min_window = s[l : r]
                    min_len = min(min_len, curr_window)
                
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    check -= 1
                l += 1
                print(check)

        return min_window

        