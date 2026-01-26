class SeatManager:

    def __init__(self, n: int):
        # min heap
        self.unres = [i + 1 for i in range(n)]

    def reserve(self) -> int:
        # if there are unreserve space
        # pop the min ele 
        # return that space
        if self.unres:
            return heapq.heappop(self.unres)
        
    def unreserve(self, seatNumber: int) -> None:
       heapq.heappush(self.unres, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)