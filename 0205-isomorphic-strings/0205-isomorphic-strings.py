class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # happy cases 
        # input: s = "egg", t = "add"
        # output: true

        # edge cases
        # input: s = "e", t = "a"
        # output: true

        # input: s = "foo", t = "bar"
        # output: false

        # input: s = "bar", t = "foo"
        # output: false

        # brute force
        # hashmap

        # low level steps
        # create a hashmap for mapping each char of s to each char of t
        # go over string s
        #   if the current char of s is in the map
        #       check if the curr corresponding char of t is not the same as the value of the map
        #       return False
        #   if it is not in the map, we need to add the curr char mapped with the curr correspondiing char of t
        #           

        # time - O(n)
        # space - O(n)
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            if s[i] in map1:
                if t[i] != map1[s[i]]:
                    return False

            else:
                map1[s[i]] = t[i] 

        for i in range(len(s)):
            if t[i] in map2:
                if s[i] != map2[t[i]]:
                    return False
            else:
                map2[t[i]] = s[i]

        return True

