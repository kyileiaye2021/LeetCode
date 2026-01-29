class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # happy cases
        # [3,2,1,5,6,4]
        # 5

        # [3,2,3,1,2,4,5,5,6], k = 4
        # [6,5,5,4,3,3,2,2,1]
        # 4

        # [1], k = 1
        # 1

        # [-9,-4,-3], k = 2
        # -4

        # [3,3,3,3,3], k = 3
        # 3

        # max heap
        # heapify the array
        # pop out the array for k times
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0

        for _ in range(k):
            res = -heapq.heappop(nums)

        return res

