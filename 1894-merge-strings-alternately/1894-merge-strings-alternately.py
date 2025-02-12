class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # happy cases
        # input - s1 = 'abc', s2 = 'pqr'
        # output - 'apbqcr'

        # edge cases
        # input - s1 = 'a', s2 = '3'
        # output - 'a3'

        # input - s1 = 'abc', s2 = 'd'
        # output - 'adbc'

        # input - s1 = 'a', s2 = 'pqr'
        # output - 'apqr'

        res = ""
        a, b = 0, 0
        while a < len(word1) and b < len(word2):
            res += word1[a] + word2[b]
            a += 1
            b += 1

        while a < len(word1):
            res += word1[a]
            a += 1

        while b < len(word2):
            res += word2[b]
            b += 1

        return res