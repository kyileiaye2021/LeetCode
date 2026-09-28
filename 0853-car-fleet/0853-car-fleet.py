class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        # create a pair of pos and speed
        # calculate the duration 
        # if the curr car takes shorter duration or equal duration to the car ahead
        #   pop the car ahead on the stack 
        #   add the curr car on the stack
        # else
        #   add the curr car on the stack

        if len(position) == 0:
            return 0
        new_arr = [[pos, spe] for pos, spe in zip(position, speed)]
        new_arr = sorted(new_arr, key=lambda x: x[0], reverse=True)
        stack = []

        for pos, spe in new_arr:
            duration = (target - pos) / spe
            stack.append(duration)
            if len(stack) >= 2: 
                curr_duration = stack[-1]
                duration_ahead = stack[-2]
                if curr_duration <= duration_ahead:
                    stack.pop()

        return len(stack)

