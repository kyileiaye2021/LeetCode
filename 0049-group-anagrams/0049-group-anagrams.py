class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Happy cases
        # input - ["eat", "tea", "tan"]
        # output - [["eat", "tea"], ["tan"]]
        
        # Edge cases:
        # input - [""]
        # output - [[""]]
        
        # input - ["a"]
        # output - [["a"]]
        
        # create a hashmap {countChar : [list of anagram]}
        # iterate over the list
        #   create a list of 0s representing the counter of a to z
        #   iterate over the curr char
        #       increment the index where the char exists by subtracting the ascii value of a from ascii value of the curr char
        #   append the curr str to the value list of corresponding list
        
        res = {}
        
        for s in strs:
            
            lst = [0] * 26
            
            for c in s:
                
                lst[ord(c) - ord('a')] += 1 # using ascii value to increment the ele indexed position
                
            lst = tuple(lst) # list cannot be the key of hashmap
            if lst not in res:
                res[lst] = [s]
            
            else:
                res[lst].append(s)
                
        return res.values()
            
        
    