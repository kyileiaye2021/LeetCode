class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapify the nums 
        # add the nums to min heap
        # pop out the nums to max heap until min heap size becomes k

        heapq.heapify(nums)
        self.k = k
        self.max_heap = []
        self.min_heap = []
        for n in nums:
            heapq.heappush(self.min_heap, n) 
        print(self.min_heap)

        # min heap (size k)
        while len(self.min_heap) > self.k:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def add(self, val: int) -> int:
        # if val is greater than the min_heap[0]
        #   add the val to min heap
        #   until the size of min heap == k
        #       pop out the ele to max heap
        # return min_heap[0]

        # if val > self.min_heap[0]:
        #     heapq.heappush(self.min_heap, val)
        #     while len(self.min_heap) > self.k:
        #         heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
        # else:
        #     heapq.heappush(self.max_heap, -val)

        # while len(self.min_heap) < k: # if the ele in min_heap 
        #     heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # return self.min_heap[0] 

        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)