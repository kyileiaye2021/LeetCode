class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # happy cases
        # nums = [1,1,1,2,2,3], k = 2
        # [1,2]

        # [1], k = 1
        # [1]

        # [1,2,1,2,1,2,3,1,3,2], k = 2
        # [1,2]

        # edge cases
        # [5], k = 1
        # 5

        # [1,1,1,2,2,2,2,3,3,3,3,3], k = 2
        # [2,3]

        # hashmap
        # add the ele in max heap
        # [(3,1), (2,2), (1,3)] (freq, ele)
        # O(nlogn) + O(klogn)

        # add the ele in min heap
        # [(2,2), (3,1)]
        # O(nlogk) time
        # O(n) space 

        # bucket sort
        # use freq count as index
        # most freq count = size of the list
        # iterate thru the new list for k times from the end
        # O(n) + O(m)space n = num of unique ele, m = most freq count
        # O(a) where a is num of ele in nums


        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        minH = [] # (freq, ele)

        for ele, freq in count.items():
            heapq.heappush(minH, (freq, ele))
            while len(minH) > k:
                heapq.heappop(minH)

        res = []
        while minH:
            freq, ele = heapq.heappop(minH)
            res.append(ele)
        
        return res






        