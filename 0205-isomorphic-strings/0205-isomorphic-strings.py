class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i]
            else:
                if s_map[s[i]] != t[i]:
                    return False
                
        for i in range(len(t)):
            if t[i] not in t_map:
                t_map[t[i]] = s[i]
            else:
                if t_map[t[i]] != s[i]:
                    return False
        return True
    
#Test cases
#s = 'egg', t= 'add', True
#s = 'foo', t = 'bar' , False
#s = 'paper', t = 'title', True

#should the size of the two strings be the same? Yes
#s = 'puppy', t = 'dead', False

#can any of the str be empty str?
# s = '', t = '', True
#can any of the str be null?
#s = None, t = None, False

#Are there any capital letters in the strings?

#Assumptions
# The size of the two strs should be the same
# There can be repetitive char in the str
# One char can map to only one another char

#High Level Plan
# *Brute Force Approach
#   Let's iterate over s. For each char in s, map it to a char in t with backtracking
# *Mapping Approach
#   iterate over s and create a map with s chars as the key and t chars as value 
#   iterate over t and create a map with t chars as the key and s chars as value
#   if the char is already in the dict, return false 

#Low level plan
#create two dictionaries
# iterate over s 
    #if the char not in the dict
        #add it to the dict
    #check the value of the curr key is the same as the ele of curr index of t
    #return false if it's not

#iterate over t
    #if char not in the dict
        #add it to the dict
    #check the value of the curr key is the same as the ele of curr index of s
    #return false if it's not
    
