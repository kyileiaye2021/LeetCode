class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap + sort + k (O(nlogn))
        # priority queue with (freq count, ele) heap -> O(n)

        freq_map = Counter(nums)
        hq = []
        
        for ele, freq in freq_map.items():
            heapq.heappush(hq, (-freq, ele))
        
        res = []
        for i in range(k):
            freq, ele = heapq.heappop(hq)
            res.append(ele)

        return res