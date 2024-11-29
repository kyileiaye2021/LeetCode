class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # happy cases
        # input: haystack = "add", needle = "ad"
        # output: 0

        # input: haystack = "sddadd", needle = 'add
        # output: 3

        # edge cases
        # input: haystack = "add", needle= "acd"
        # output: -1

        # plan

        # i, j = 0, 0
        # k = 0
        # iterate until j reaches the end of needle an k reaces the end of the haystack
        #   check if k ele is the same as j ele
        #       increment k and j by 1
        #   else: 
        #       replace i by k pointer 
        #       j = 0
        # check if i is equal to len(haystack)
        #   return -1
        # return i

        # sliding window

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i+len(needle)] == needle:
                return i

        return -1