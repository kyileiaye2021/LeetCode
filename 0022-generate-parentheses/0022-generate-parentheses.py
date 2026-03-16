class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open == n and close == n:
        #   add curr str to res
        # if open < n:
        #   if we go left, add '(' to curr str
        #       increment open
        # remove the added '(' from curr str
        # decrement open
        # if open > close:
        #   if we go right, add ')' to curr str
        #       increment close
        open = close = 0
        res = []
        cur_str = []

        def recur(open, close):
            # base case
            if open == n and close == n:
                res.append(''.join(cur_str))
                return

            # left 
            if open < n:
                cur_str.append('(')
                recur(open + 1, close)
                # backtrack
                cur_str.pop()

            # right
            if close < open:
                cur_str.append(')')
                recur(open, close + 1)
                cur_str.pop()

        recur(open, close)
        return res



        

    

        