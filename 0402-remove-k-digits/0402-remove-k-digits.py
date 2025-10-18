class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        # stack to keep track of eles to be remvoed
        # iterate thru the str
        #   convert the char to int
        #   while stack and stack last ele > curr int and k > 0
        #       pop the last ele from the stack
        #   add the curr int to the stack
        # join the stack and return the str

        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:len(stack) - k]
        res_str = ''.join(stack)
        return str(int(res_str)) if res_str else "0"
        