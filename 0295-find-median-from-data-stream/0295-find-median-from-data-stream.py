class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        if (self.maxheap and self.minheap and (-1 * self.maxheap[0]) > self.minheap[0]):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        
        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        
            if len(self.maxheap) == len(self.minheap):
                median = (-self.maxheap[0] + self.minheap[0]) / 2
            elif len(self.maxheap) > len(self.minheap):
                median = -self.maxheap[0]
            else:
                median = self.minheap[0]

            return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()