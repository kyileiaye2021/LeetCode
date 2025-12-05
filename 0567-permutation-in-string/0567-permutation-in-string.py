class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # happy cases
        # s1 = "a", s2 = "eab"
        # true

        # s1 = "ab", s2 = "ebag"
        # true

        # s1 = "abc", s2 = "acbaaab"
        # true

        # edge cases
        # s1 = "a", s2 = "a"
        # true

        # s1 = "ab", s2 = "a"
        # false

        # s1 = "aaa", s2 = "abaab"
        # false

        # two pointers
        # hashmap for s1
        # create hashmap for substr of len s1 in s2
        # check if s1 dict == s2 dict return true
        # l and r - 0, len(s1)
        # iterate thru the s2 while r < len(s2)
        #   remove l ele from s2 dict
        #   add r ele to s2 dict
        #   check if s1 dict == s2 dict
        #       return True
        # return False

        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:len(s1)])
        if s1_dict == s2_dict:
            return True

        l, r = 0, len(s1)
        while r < len(s2):
            s2_dict[s2[l]] -= 1
            s2_dict[s2[r]] += 1
            if s1_dict == s2_dict:
                return True
            r += 1
            l += 1
        return False
