class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # start from empty
        # open = 0

        # recur()
        # if open == n and close == n:
        #   create a cur list copy and add it to res

        # go to left -> '('
        # open += 1
        # pop the curr ele
        # open -= 1
        # go to right -> ')'
        # while open == n and close < n:
        #   go to right -> ')'

        cur_lst = []
        res = []

        def recur(open, close):
            if open == n and close == n:
                res.append(''.join(cur_lst))

            if open < n:
                cur_lst.append('(')
                recur(open + 1, close)
                cur_lst.pop()

            if close < open:
                cur_lst.append(')')
                recur(open, close + 1)
                cur_lst.pop()

        recur(0, 0)
        return res



