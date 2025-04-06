class RecentCounter:

    # edge case
    # input: ["RecentCounter"], [[]]
    # output: [null]

    # input: ["RecentCounter", "Call"], [[], [1]]
    # output: None

    # input: ["RecentCounter", "Ping"], [[9], [1]]
    # output: None

    def __init__(self):
        # initialize the counter with zero requests
        self.deque = []
        
    def ping(self, t: int) -> int:
        # check if t > last ele in deque
        #   add t to the deque
        # find range [p,q]
        # p = t - 3000
        # q = t
        # check if the first ele of deque is not >= p and <= q
        #   pop the first ele from deque
        # return the deque 

        if len(self.deque) == 0:
            self.deque.append(t)
            return len(self.deque)

        last = self.deque[-1]
    
        if t > last:
            self.deque.append(t)

        p = t - 3000
        q = t

        
        count = 0
        for i in range(len(self.deque)):
            
            if self.deque[i] < p:
                count += 1
            else:
                break
        

        for i in range(count):
            self.deque.pop(0)

        return len(self.deque)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)