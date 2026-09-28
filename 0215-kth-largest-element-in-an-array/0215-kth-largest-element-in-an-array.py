class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # minheap
        # iteraete thru nums
        #   add curr n to min heap
        #   if min heap size > k
        #       pop min heap
        # return min heap first ele
        # O(nlogk) time, O(k) space

        # min_heap = []
        # for n in nums:
        #     heapq.heappush(min_heap, n)
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # return min_heap[0]

        # convert all elements to - nums 
        # heapify it
        # for k times, heappop the max heap
        # O(n + klogn) time, O(n) space

        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            res = -heapq.heappop(max_heap)

        return res

