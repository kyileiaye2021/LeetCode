class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # happy case
        # input = "ab", k = 2
        # output = "ba"

        # edge cases
        # input = "a", k = 1
        # output = "a"

        # input = "ab", k = 3
        # output = "ba"

        # input = "abc", k = 2
        # output = "bac"

        # brute force
        # iterate thru the list and for each window swap the chars 
        s = list(s)

        a = 0
        while a < len(s):
            i = a
            j = a + k - 1
            if j >= len(s):
                j = len(s) - 1

            while i < j:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            
            a += (k * 2)
        s = "".join(s)
        return s

        # Space - O(n)
        # Time - O(nlogn)