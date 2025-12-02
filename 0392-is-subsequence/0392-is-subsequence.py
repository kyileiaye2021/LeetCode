class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # happy case
        # s = "abc", t = "abcd"
        # true

        # s = "abc", t = "xacbd"
        # false
        
        # edge case
        # s = "abc", t = ""
        # false

        # s = "", t = "abc"
        # true

        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #   check if curr i ele == curr j ele
        #       move i and j
        #   else
        #       move j
        # return true if i >= len(s) else false

        i, j = 0, 0
        s_len = len(s)
        t_len = len(t)

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i >= s_len else False
            
