class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # happy cases
        # text1: "abc", text2: "abcd"
        # output: 3

        # text1 : abcde, text2:ace
        # output: 3

        # text1: aa, text2:abb
        # output: 1

        # text1:"", text2:""
        # output: 0

        # text1: "ab", text2:""
        # output:0

        # text1: "", text2: "ab"
        # output:0

        # text1: "abc", text2: "ef"
        # output: 0

        # text: "abcde", text2: "eac"
        # output: 2

        # hashmap?
        # create hashmap for both text1 and text2
        # iterate thru the shorter text
        #   check if the curr ele is in the other text hashmap
        #       increment the count
        #       decrement that ele freq in the other text hashmap
        # hashmap won't work since we have to care about order

        # two pointers?
        # i and j at the beginning of two textes
        # check if the two are equal
        #   increment the count
        #   move i and j by 1
        # check if which one is smaller alphabetically and move that pointer
        # return the count
        # this doesn't work because it doesn't find the optimal solution if chars are not in order in one text

        # dynamic programming
        # create 2D array

        # iterate thru the text1 (i)
        #   iterate thru the text2 (j)
        #       if the chars are equal 
        #           update the curr entry with the diagonal ele + 1
        #       else
        #           update the curr entry with max of (above entry or left entry)
        # in the matrix, get the largest num and return

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        print(dp)

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        print(dp)
        max_subseq = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                max_subseq = max(dp[i][j], max_subseq)
        return max_subseq