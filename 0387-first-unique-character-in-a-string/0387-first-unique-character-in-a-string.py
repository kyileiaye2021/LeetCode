class Solution:
    def firstUniqChar(self, s: str) -> int:
        #create frequency map for each ele and fill it up
        
        frequency = {}
        
        for ele in s:
            if ele not in frequency:
                frequency[ele] = 1
            else:
                frequency[ele] += 1
                
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1
    