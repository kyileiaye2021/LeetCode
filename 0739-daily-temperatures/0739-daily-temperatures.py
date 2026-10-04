class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # stack
        # iterate thru the temperatures
        #   while stack and stack[-1] < cur temp
        #       pop the stack
        #       add the diff between temp and popped ele to popped index
        #   add the curr to the stack

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            while stack and stack[-1][0] < t:
                temp, idx = stack.pop()
                res[idx] = i - idx

            stack.append((t, i))
        
        return res
