class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap

        distances = [(math.sqrt(p**2 + q**2), [p, q]) for p, q in points]
        heapq.heapify(distances)
        res = []

        for _ in range(k):
            dist, coor = heapq.heappop(distances)
            res.append(coor)
        
        return res
