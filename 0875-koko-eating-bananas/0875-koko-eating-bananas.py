class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            time = 0
            for b in piles:
                time += math.ceil(b / mid)
            
            if time > h:
                low = mid + 1
            
            else:
                res = mid
                high = mid - 1

            # else:
            #     return mid

        return res

        