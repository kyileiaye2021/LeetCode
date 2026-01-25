class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # happy cases
        # nums = [1,1,1,2,2,3], k = 2
        # output: [1,2]

        # nums = [1,1,3,-2,-5], k = 1
        # output: 1

        # nums = [3,4,-1,3], k = 2
        # output: [3,4,-1]

        # edge case
        # nums = [1,2,3,4], k = 3
        # output: [1,2,3]

        # nums = [2,2,1,1], k = 1
        # output: 1 or 2

        # nums = [2,2,1,1], k = 2
        # output: [1,2]

        # max heap (freq count, ele)
        # [(3,1), (2,2), (1,3)]
        # for k times
        # pop out the max heap and store the ele to the res
        # return res

        max_heap = []
        res = []
        ele_count = Counter(nums) #{1: 3, 2:2, 3: 1}

        max_heap = [(-count, ele) for ele, count in ele_count.items()]
        heapq.heapify(max_heap)

        for _ in range(k):
            freq, ele = heapq.heappop(max_heap)
            res.append(ele)

        return res




