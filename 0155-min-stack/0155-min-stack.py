class MinStack:
    # we need to get the min val in stack with O(1) time
    # we can use extra stack data structure to maintain the curr min val for each val in the orig stack
    # so, the min val would be at the top of the stack and each time the ele is popped out of the orig stack, we also need to pop out of the min stack

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        if self.minStack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return null

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return null


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()