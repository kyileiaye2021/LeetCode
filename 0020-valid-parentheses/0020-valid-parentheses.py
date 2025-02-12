class Solution:
    def isValid(self, s: str) -> bool:
        # using stack
        # using dict

        map = {'(':')', '{':'}', '[':']'}
        open_stack = []

        for ele in s:
            if ele in map:
                open_stack.append(ele)

            else:
                if open_stack:
                    last_ele = open_stack.pop()
                    if map[last_ele] != ele:
                        return False

                else:
                    return False

        if not open_stack:
            return True

        else:
            return False
