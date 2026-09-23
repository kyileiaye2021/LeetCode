class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        # res = -1
        # if m *k > len(bloomDay)
        #   return res

        # happy cases
        # bloomDay = [1,10,3,10,2], m = 3, k = 1
        # 3

        # edge cases
        # bloomDay = [1,10,3,10,2], m = 3, k = 2
        # -1

        # bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
        # 12

        # l = min(bloomDay)
        # r = max(bloomDay)
        # while l < = r:
        #   mid = (l + r) // 2
        #   bouquet = 0
        #   streak = 0 (to keep track of the num of continuous flower)
        #   for b in bloomDay
        #       if b <= mid 
        #           streak += 1
        #           if streak == k:
        #               bouquet += 1
        #               streak = 0
        #       else:
        #           streak = 0
        #   if bouquet >= m:
        #       res = mid
        #       r = mid - 1
        #   eles:
        #       l = mid + 1
        # return res

        res = -1
        if m * k > len(bloomDay):
            return res

        l = min(bloomDay)
        r = max(bloomDay)

        while l <= r:
            mid = (l + r) // 2
            bouquet = 0
            streak = 0

            for b in bloomDay:
                if b <= mid:
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
            
        return res
