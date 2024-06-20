class Solution:
    def romanToInt(self, s: str) -> int:
        #create a map {roman ele : numerical val}
        #create a var to store the total numerical val
        #iterate over the str s
            #check the next index still within the range of bound and the curr char val < next char val
                #subtract the curr char val from the total numerical val
            #add the curr char val to the total numerical val
        #return total numerical val
        
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000   
        }
        total_numerical_val = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total_numerical_val -= roman[s[i]]
            else:
                total_numerical_val += roman[s[i]]
                
        return total_numerical_val