class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        depth = 0

        for paren in s:
            if paren == '(':
                if depth != 0:
                    res += paren
                depth += 1

            else:
                depth -= 1
                if depth != 0:
                    res += paren

        return res