class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # asking the speed
        largest = max(piles)
        # for i in range(1, largest + 1):
        #     print("i: ", i)
        #     total = 0

        #     for p in piles:
        #         time_taken = ceil(p / i)
        #         total += time_taken

        #     if total <= h:
        #         return i

        l = 1
        r = largest
        best = 0

        while l < r:
            mid = (l + r) // 2

            total = 0
            for p in piles:
                time_taken = ceil(p / mid)
                total += time_taken

            
            if total <= h: # faster speed
                # need to decrease rate
                # best = mid
                r = mid

            elif total > h: # slow speed
                # need to increase rate
                l = mid + 1
            
            # else:
            #     return mid

        return r

