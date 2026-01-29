class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [1,2,3,4,5], k = 4, x = 3
        # [2, 1, 0, 1, 2]
        # [1,2,3,4]

        # [1,1,2,3,4,5], k = 4, x = -1
        # 2, 2, 3, 4, 5, 6
        # [1,1,2,3]

        # [1], k = 1, x = 9
        # [1]

        # [0,1,1,2,2]
        # [3,2,4,1,5]
        
        # [(dist, ele)]
        # [ele]

        # min heap for dist
        # dist_heap = []
        # for ele in arr:
        #     dist = abs(ele - x)
        #     heapq.heappush(dist_heap, (dist, ele))

        # # min heap for first k ele
        # closet_heap = []
        # for _ in range(k):
        #     dist, ele = heapq.heappop(dist_heap)
        #     heapq.heappush(closet_heap, ele)

        # res = []
        # while closet_heap:
        #     res.append(heapq.heappop(closet_heap))
        
        # return res

        l = 0
        r = len(arr) - k
        
        while l < r:
            mid = (l + r) // 2

            diff1 = abs(arr[mid] - x)
            diff2 = abs(arr[mid + k] - x)

            # if r+1 ele is closer to x than the l ele
            # move the window to right
            if diff1 > diff2:
                l = mid + 1

            # if l ele is closer to x than r+1 ele (or) if the diff is the same, we have to take the smaller ele
            else:
                r = mid
            
        
        return arr[l : l + k]

