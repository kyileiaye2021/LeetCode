class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Happy cases
        # input: s = 'abc'
        # output: 0

        # input: s = 'aab'
        # output: 2

        # Edge cases
        # input: s = 'a'
        # output: 0

        # input: s = "aa"
        # output: -1

        # bruteforce
        # hashmap
        # Two pointer 
        # Sliding window

        # create an empty hashmap
        # populate the hashmap 
        # itereate over ele in the str
        #   check if the curr ele freq val is 1
        #       return its index
        
        # time - O(2n)
        # space - O(n)

        freq = {}
        for ele in s:
            if ele in freq:
                freq[ele] += 1

            else:
                freq[ele] = 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1