class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Happy cases
        # input - ran = "aa", mag = "aab"
        # ouput - true
        
        # Edge cases
        # input - ran = 'a', mag = 'b'
        # output - false
        # input - ran = "a", mag = 'a'
        # output - true
        # input - ran = 'aaa', mag = 'abab'
        # output - false
        
        # Hashmap Approach
        # create a hashmap for magazine 
        # iterate over the magazine and fill up the key and freq value
        # iterate over the ransomNote
        #   check if the curr ele is in the hashmap
        #       check if the freq val is > 0
        #           decrement the freq value of that key
        #       else:
        #           return false
        #   else: return false
        # return True
        
        map = {}
        for ele in magazine:
            if ele not in map:
                map[ele] = 1
            else:
                map[ele] += 1
                
        for ele in ransomNote:
            if ele in map:
                if map[ele] > 0:
                    map[ele] -= 1
                else:
                    return False
            else:
                return False
        
        return True
        # Time complexity - O(m + n)
        # Space complexity - O(n)