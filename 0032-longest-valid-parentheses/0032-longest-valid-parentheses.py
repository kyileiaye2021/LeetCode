class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # happy cases
        # "(())"
        # 4
        # 
        # "()(()"
        # 2

        # "()()((()"
        # 4

        # edge cases
        # "(((("
        # 0

        # "))))"
        # 0

        # ")()()("
        # 4

        # ""
        # 0

        # "("
        # 0

        # "(()())"
        # 6
        
        # stack
        # max_len
        # cur_len
        # start = -1
        # iterate thru the ele
        #   if ele i == "("
        #       add i to stack
        #   else
        #       if stack
        #           open_i = pop the last stack
        #           cur_len = i - start
        #           max_len = max(cur_len, max_len)
        #       else:
        #           start = i + 1
        # return max_len

        max_len = 0
        cur_len = 0
        start = -1
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            
            else:
                if stack:
                    open_i = stack.pop()
                    if stack:
                        # there are still unmatched (
                        cur_len = i - stack[-1]
    
                    else:
                        cur_len = i - start
                    max_len = max(max_len, cur_len)
                else:
                    start = i 
        
        return max_len





        