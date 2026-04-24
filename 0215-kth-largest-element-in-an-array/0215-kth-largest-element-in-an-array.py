class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [3,2,1,5,6,4], k = 2
        # 5

        # nums = [3,2,3,1,2,4,5,5,6], k = 4
        # [6,5,5,4,3,3,2,2,1], 4

        # sort the arr --> O(nlogn)
        # bucket sort --> O(n)
        # maxheap --> O(klogn)

        hq = [-n for n in nums]
        heapq.heapify(hq)

        res = 0
        for _ in range(k):
            res = -heapq.heappop(hq)

        return res