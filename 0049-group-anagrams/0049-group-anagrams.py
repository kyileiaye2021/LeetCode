class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # happy cases
        # input: ["a", "a", "b"]
        # output: [["a", "a"], ["b"]]

        # edge cases
        # input: [""]
        # output: [[""]]

        # nested for + hashmap O(n^2)
        # hashmap {{'e': 1, 'a': 1, 't': 1}: [eat, ate, tea]
        #           {'b':1, 'a':1, 't':1}: ["bat"]
        #           {'t':1, 'a':1, 'n':1}: ["nat", "tan"]}
        
        # a-z chars : 26 chars --> 10001....
        main_hashmap = {}
        for s in strs:
            # temp list with 26 0s (0-25)
            temp_lst = [0] * 26

            # iterate thru the s
            for c in s:

            #   get the index of cur char in temp list
                idx = ord(c) - ord('a')

            #   put 1 at that position
                temp_lst[idx] += 1

            # hashed_str = combine temp list into a str
            hashed_str = ''.join(str(temp_lst))

            # add the s to main_hashmap with hashed_str  {hashed_str: [s]}
            if hashed_str not in main_hashmap:
                main_hashmap[hashed_str] = [s]
            else:
                main_hashmap[hashed_str].append(s)

        res = []
        for hashed_str, group in main_hashmap.items():
            res.append(group)

        return res






       