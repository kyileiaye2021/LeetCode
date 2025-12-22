class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "abcde", s2 = "abeuelkj"
        # false

        # s1 = "bc", s2 = "abbccbter"
        # true

        # s1 = "a", s2 = "abb"
        # true

        # s1 = "avb", s2 = "bb"
        # false

        # s1 = "hh", s2 = "ahgu"
        # false

        # hashmap for s1
        # iterate thru the s2
        #   if curr ele not in s1 hashmap
        #       reset the hashmap to empty hashmap
        #       moving l and r
        #   else
        #       adding the curr ele to s2 hashmap
        #       move the right ele
        #       if hashmap == s1 hashmap
        #           return true
        # return false

        s1_hashmap = Counter(s1)
        k = len(s1)
        s2_hashmap = Counter(s2[:k])
        if s1_hashmap == s2_hashmap:
            return True

        for i in range(k, len(s2)):
            s2_hashmap[s2[i - k]] -= 1
            if s2_hashmap[s2[i - k]] == 0:
                del s2_hashmap[s2[i - k]] 

            s2_hashmap[s2[i]] = s2_hashmap.get(s2[i], 0) + 1
            if s1_hashmap == s2_hashmap:
                return True

        return False
