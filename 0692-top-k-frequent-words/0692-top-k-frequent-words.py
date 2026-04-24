class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # freq map {str -> freq}
        # max heap
        # (freq, str)

        freq_map = Counter(words)
        max_heap = [(-f, w) for w, f in freq_map.items()]
        heapq.heapify(max_heap)

        res = []
        for _ in range(k):
            freq, w = heapq.heappop(max_heap)
            res.append(w)

        return res