class Solution:
    def decodeString(self, s: str) -> str:
        
        # stack
        # iterate thru the s
        #   add the curr char if s curr char is not ]
        #   if curr char is ]
        #       pop the last ele out while the last ele != [
        #       create a substr with those popped ele
        #       pop the [
        #       while last ele of stack != digit
        #           pop the last ele and create a digit
        #       multiply digit and substr and add it back to stack
        # return combination of stack

        stack = []
        for char in s:
            if char != ']':
                stack.append(char)

            else:
                # popping chars
                substr = ''
                while stack and stack[-1] != '[':
                    curr_char = stack.pop()
                    substr = curr_char + substr

                stack.pop() # popping [ char

                # popping digits
                k = ''
                while stack and stack[-1].isdigit():
                    curr_digit = stack.pop()
                    k = curr_digit + k

                stack.append(int(k) * substr)

        return ''.join(stack)



