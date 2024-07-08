class Solution:
    def isValid(self, s: str) -> bool:
        
        #Can there be empty string?: no
        #({[]}) #true
        #(){}[] #true
        
        '''
        Stack and hashmap
        * create a hashmap {closing parenthesis : opening parenthesis}
        * create a stack to store opening parenthesis in the str
        * iterate over the string
            * check if the curr char is in the hashmap
                * check if the last item of the stack is the corresponding opening                     parenthesis of the curr char
                    * get rid of that opening parenthesis from the stack
                * if the closing parenthesis doesn't have opening parenthesis
                    * return False
                
            * if the curr char is not in hashmap (open parenthesis)
                * put it in the stack
        * return True if there is no ele in the stack
        '''
        
        open_paren_stack = []
        parenthesis_map = {')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c in parenthesis_map: #if the curr char is close parenthesis
                if open_paren_stack and open_paren_stack[-1] == parenthesis_map[c]:
                    open_paren_stack.pop()
                
                else:
                    return False
            else: #if the curr char is open parenthesis
                open_paren_stack.append(c)
            
        if len(open_paren_stack) == 0:
            return True
        else:
            return False
        
                
                
        