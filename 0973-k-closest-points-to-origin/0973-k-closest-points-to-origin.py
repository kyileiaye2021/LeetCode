class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap

        # distances = [(math.sqrt(p**2 + q**2), [p, q]) for p, q in points]
        # heapq.heapify(distances)
        # res = []

        # for _ in range(k):
        #     dist, coor = heapq.heappop(distances)
        #     res.append(coor)
        
        # return res


        # O(n + klogn) time
        # O(n) space

        hq = []
    
        for p, q in points:
            dist = p**2 + q**2
            heapq.heappush(hq, (-dist, [p,q]))

            while len(hq) > k:
                heapq.heappop(hq)

        res = [coor for dist, coor in hq]
        return res

            
