class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # input: [3,2,1,5,6,4], k = 2
        # output: 5

        # input: [1,1,2], k = 2
        # output: 1

        # input: [1], k = 1
        # output: 1

        # input [1,2,3,3], k = 2
        # output: 3

        # heap
        # heapify the nums
        # while len of heap is greater than k 
        #   pop out the ele from heap
        # return 1st ele in heap

        heapq.heapify(nums)
        print(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]