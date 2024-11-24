class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # happy cases
        # input: s = "ana", t= "naa"
        # output: true

        # input: s = "tab", t = "bar"
        # output: false

        # edge cases
        # input: s = "aa", t = "a"
        # output: false

        # input: s = "a", t = "ab"
        # output: false

        # hashmap 

        # create a hashmap for t str
        # iterate over the ele in s
        #   check if the curr ele is not in t hashmap
        #       return false 
        #   else:
        #       check if the curr key ele freq val is greater than 0 
        #           decrement that freq val by 1
        #       else:
        #           return false
        # check if the ele in the hashmap still has freq val of more than 1
        # return True

        t_map = {}

        for ele in t:
            if ele not in t_map:
                t_map[ele] = 1
            else:
                t_map[ele] += 1

        for ele in s:
            if ele not in t_map:
                return False
            if t_map[ele] > 0:
                t_map[ele] -= 1
            else: 
                return False

        for ele in t_map:
            if t_map[ele] > 0:
                return False
        
        return True






        