class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ele in ransomNote:
            if ele in magazine:
                magazine = magazine.replace(ele, "",1)
            else:
                return False
        return True
            
#ransomNote = 'a', magazine = "a", True
#ransomNote = 'b', magazine = 'a', False

#Would the letters be case sensentive?  Yes
#ransomNote = 'aB', magazine = 'ab' False

#Is it possible that ransomNote has different length than magazine? Yes
#ransomNote = 'aa', magazine = 'aab', True

#edge cases
#Can both strings be empty?
#ransomNote = "", magazine = "", True
#ransomNote = '', magazine = "a", False
#ransomNote = 'a', magazine = '', False

#Can either of the strings be null? (will be invalid)
#ransomNote = None, magazine = None, False

#can strings have repetitive letters? 
#ransomNote = 'aa', magazine = 'aab', True

#Assumption:
# Letters can be repetitive in strings
# Letters are case sentitive
# The lengths of the strs can be different
# THe strings can be empty
# None values will be invalid

#High Level Planning
# *Iterative Approach
#   *iterate over the ransomNote. for each char in ransomNote, check if the char 
#    is in magazine, remove it from magazine. if it doesn't exist, return False 
#    immediately
# *Frequency Counting Approach 1
#   *iterate over the ransomNote and create a frequency count of each letter in 
#   dictionary. iterate over the magazine and create another frequency count of each 
#   letter in dictionary. compare those dictionary
# *Iterative Approach 2
#   *iterate over the ransomNote and for each char in ransomNote, check if it's in 
#   the magazine, remove it from magazine to ensure that it will not be double counted

# Low Level Planning
# *Iterative Approach 2
# itereate over the ransomNote
    # check if the curr char in magazine
        #remove the curr char from magazine
    #return False immediately
    
#return True




