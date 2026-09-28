class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index_map = {char: i for i, char in enumerate(s)}
        stack = []
        # in_stack = set()

        for i, char in enumerate(s): 
            if char not in stack:
                while stack and stack[-1] > char and i < last_index_map[stack[-1]]:
                    # in_stack.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                # in_stack.add(char)
            else:
                continue
        
        return ''.join(stack)