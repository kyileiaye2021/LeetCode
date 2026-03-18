class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # num of flowers = m * k
        # if len of bloomDay < nun of flowers
        #   return -1

        # iterate i from 1 to max day
        #   iterate j thru the arr from 0 to n -k
        #       from j to j + k
        #           check all ele are <= curr i
        #           m -= 1
        #       if m == 0:
        #           res = i
        #           break
        # return res if m = 0 else -1


        l = 1
        r = max(bloomDay)
        res = -1

        while l <= r:
            bouquet = 0
            streak = 0
            mid = (l + r) // 2

            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    streak += 1
                    if streak == k:
                        bouquet += 1
                        streak = 0
                else:
                    streak = 0

            if bouquet >= m:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        print(bouquet)
        return res 




