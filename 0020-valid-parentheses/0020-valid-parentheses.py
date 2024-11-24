class Solution:
    def isValid(self, s: str) -> bool:
        # happy cases
        # input: s = "()"
        # output: true

        # input: s = "(}"
        # output: false

        # input: s = "({)}"
        # output: false

        # edge cases
        # input: s = "("
        # output: false

        # input: s = "}"
        # output: false

        # input: "}{"
        # output: false

        # hashmap {'(':")"}
        # create a stack
        # iterate over the char in the str
        #   if the cur char is open bracket
        #       add it to the stack
        #   else:
        #       check if the stack is not empty and the current last char of stack matches the close bracket
        #           pop that last ele 
        #       else: return false


        map = {'(': ')', '{': '}', '[':']'}
        open_brackets = []

        for ele in s:
            if ele in map: # open brackets
                open_brackets.append(ele)
            else: # close brackets
                if len(open_brackets) > 0:
                    last = open_brackets[-1]
                    if ele == map[last]:
                        open_brackets.pop()
                    else: 
                        return False
                else:
                    return False

        if len(open_brackets) > 0:
            return False
        return True




