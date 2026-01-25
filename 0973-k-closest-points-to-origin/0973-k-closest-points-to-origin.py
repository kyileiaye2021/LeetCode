class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap (dist, [point])
        # find the dist from origin
        # add the dist and points to min heap 

        # pop out the dist and points for k times
        # store in res
        # return res

        min_heap = []
        for p, q in points:
            dist = sqrt(p**2 + q**2)
            min_heap.append((dist, [p, q]))

        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            res.append(point)

        return res

        