class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # dfs(open, close)
        # base case
        # if open > n
        #   return (don't expand)
        # if close > opening parenthesis num
        #   return (don't expand)
        # if open == n and close num
        #   put the curr parenthesis str to the res arr
        # dfs(open + 1, close) # add opening parenthesis
        # backtrack --> pop the curr '(' from res
        # dfs(open, close) # add closing parenthesis
        res = []
        def dfs(open, close, curr):

            if open == n and close == n:
                cur_paren = ''.join(curr)
                res.append(cur_paren)
                return

            if open < n:
                curr.append('(')
                dfs(open + 1, close, curr)   
                curr.pop() # backtrack

            if close < open:
                curr.append(')')
                dfs(open, close + 1, curr)     
                curr.pop()

        dfs(0,0,[])
        return res
        