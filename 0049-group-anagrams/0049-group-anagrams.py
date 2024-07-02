class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a dict to store { count of the num of ele : [list of anagrams]}
        #iterate over the list
            # iterate over the curr str
            #   count the num of each curr char 
            # append the str to the value of the dict key
            
        res = defaultdict(list) #values are gonna be list
        
        for s in strs:
            
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            res[tuple(count)].append(s) #list cannot be key in python so make it tuple
            
        return res.values()
                