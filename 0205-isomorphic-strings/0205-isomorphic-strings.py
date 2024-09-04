class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Happy cases:
        # input: s="egg", t = "add"
        # output = true
        
        # Edge cases
        # input: s = "e", t = 'g'
        # output - true
        # input: s = 'e', t = 'gh'
        # output - false
        # input: s = 'foo', t = 'bar'
        # output - false
        # input: s = 'bar', t = 'foo'
        # output - false
        
        #  if the len of s and t are not equal, return False
        # create a hashmap for s 
        
        #   iterate over s
        #       check if the curr ele of s is in hashmap
        #           check if the mapped value of curr ele is not equal to the curr t ele
        #               return false
        #       set hashmap[s] = curr t ele
        
        # create a hashmap for t
        # iterate over the ele in t
        #    check if the curr ele of t is in hashmap
        #       check if the mapped value of curr ele is not equal to the curr s
        #           return false
        #    set hashmap[t] = curr s ele
        # return True
        
        if len(s) != len(t):
            return False
        
        s_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                if t[i] != s_map[s[i]]:
                    return False
            else:
                s_map[s[i]] = t[i]
        
        t_map = {}
        for i in range(len(t)):
            if t[i] in t_map:
                if s[i] != t_map[t[i]]:
                    return False
            else:
                t_map[t[i]] = s[i]
        
        return True