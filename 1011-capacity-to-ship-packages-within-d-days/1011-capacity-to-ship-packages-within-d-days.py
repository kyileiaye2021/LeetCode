class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            d = 1
            total = 0
            for w in weights:
                total += w
                if total > mid:
                    total = w
                    d += 1

            if d > days:
                l = mid + 1

            else:
                res = mid
                r = mid - 1
        return res
        

        