class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # s = "egg", t = "add"
        # true

        # s = "foo", t = "bar"
        # false

        # s = "bar", t = "foo"
        # false   

        # s = "bad", t = "felt"
        # false

        # s = "felt", t = "bad"
        # false

        # hashmap
        # s_map = {e:a, g:d}, t_map = {a:e, d:g}     
        # check if the size of the two inputs are not the same -> return false
        # iterate thru the s
        #   check if the ele is in s_map
        #       check if the value of the curr key is not the same
        #           return False
        #   else
        #       check if the curr t is already in the t map
        #           return false
        # return true

        s_map = {}
        t_map = {}

        s_len = len(s)
        t_len = len(t)

        # if s_len != t_len:
        #     return False

        for i in range(s_len):
            if s[i] in s_map:
                if s_map[s[i]] != t[i]:
                    return False

            else:
                if t[i] in t_map:
                    return False

                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]

        return True