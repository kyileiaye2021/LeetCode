class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # happy cases
        # input: s = "AAAAACCCCCAAAAACCCCCAAAAA"
        # output: "AAAAACCCCC", "CCCCCAAAAA"

        # input: s = "AAAAAAAAAAAAAA"
        # output: "AAAAAAAAAA"

        # edge cases
        # input: s = "AAA"
        # output: None

        # input: s = "ACATGGATGCCCATA"
        # output: None

        # use set 
        # iterate thru the ele in the str upto len - 10
        #   make a window of size 10 starting from the curr ele
        #   check if the substr is in the set
        #       add it to the res list
        # return the res list
        unique_substr = set()
        res = set()

        n = len(s)
        if n <= 10:
            return list(res)

        for i in range(n - 9):
            curr_window = s[i: i + 10]
            if curr_window in unique_substr:
                res.add(curr_window)
            else:
                unique_substr.add(curr_window)

        return list(res)
