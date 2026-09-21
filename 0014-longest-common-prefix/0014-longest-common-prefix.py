class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # res 
        # iterate thru the chars in first ele
        #   iterate thru the strs
        #       if curr char of first ele != the curr char of s or s is out of bound
        #           return res
        #   add curr char of first ele to res
        # return res

        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]

        return res
