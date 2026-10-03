class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # binary search
        
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            rate = l + ((r - l) // 2)
            total = 0
            for p in piles:
                total += math.ceil(p / rate)

            if total > h:
                l = rate + 1
            else:
                res = rate
                r = rate - 1

        return res

            