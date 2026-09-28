class Solution:
    def removeDuplicates(self, s: str) -> str:
        # happy cases
        # "abbaca"
        # "ca"

        # s = "azxxzy"
        # "ay"

        # edge cases
        # "a"
        # 'a"

        # "abc"
        # "abc"

        # "abba"
        # ""

        # "aba"
        # "aba"

        # "bbb"
        # 'b'

        # 'bbbb'
        # ''

        # stack
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()

            else:
                stack.append(char)

        return ''.join(stack)