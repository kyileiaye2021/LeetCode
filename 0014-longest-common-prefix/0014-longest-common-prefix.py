class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Happy case
        # input: strs = ["ab", "abc", "abd"]
        # output: "ab"

        # input: strs = ["abc", "abd", "ace"]
        # output: "a"

        # Edge case
        # input: str = ["ab", "cd", "de"]
        # output: ""

        # input: str = ["abc"]
        # output: ""

        # input: str = ["ab", "ab"]
        # output: "ab"

        # two pointers
        # initialize common to first ele 
        # iterate thru the list
        #   l,r both at 0
        #   l pointing to first ele in common
        #   r pointing to first ele in curr str
        #   until one of the pointers reaches the end
        #       check if the curr pointer vals are not the same
        #           break the loop
        #   update the common str with common[:l]
        # return common
    
        common = strs[0]
        for s in strs:
            l,r = 0, 0
            while l < len(common) and r < len(s):
                if common[l] != s[r]:
                    break
                l += 1
                r += 1
            common = common[:l]

        return common