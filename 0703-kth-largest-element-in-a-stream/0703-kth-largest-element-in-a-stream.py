class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapify the nums 
        # add the nums to min heap
        # pop out the nums to max heap until min heap size becomes k

        heapq.heapify(nums)
        self.k = k
        self.min_heap = []
        for n in nums:
            heapq.heappush(self.min_heap, n) 
        print(self.min_heap)

        # min heap (size k)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int: 

        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)