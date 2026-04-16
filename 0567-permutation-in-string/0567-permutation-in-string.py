class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 = "abcb", s2 = "eibdbbacoo"
        # true

        # s1 = "abcb", s2 = "eidbdadc"
        # false

        # s1 = "ba", s2 = "eid"
        # false

        # s1 = "", s2 = "gg"
        # true

        # s1 = "hello", s2 = ""
        # false

        # s1 = "", s2 = ""
        # true

        # sliding window with 2 pointers
        if len(s1) > len(s2):
            return False

        # hashmap for s1
        # iterate thru s2
        #   if cur char not in s1 hashmap
        #       move i and j
        #   else
        #       decrement the curr char freq in s1 hashmap
        #       move j
        #       

        # k = len(s1)
        # check first k ele 

        # iterate from k to the end
        #   create hashmap for each window
        #   check the hashmap are the same
        #       return true
        
        k = len(s1)
        s1_hashmap = Counter(s1)
        
        for i in range(len(s2) - k + 1):
            if Counter(s2[i: i +k]) == s1_hashmap:
                return True

        return False










        