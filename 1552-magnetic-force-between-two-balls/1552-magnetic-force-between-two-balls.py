class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # possible force - 1-(max - min)

        # l = 0
        # r = max - min
        # while l < r
        #   find mid
        #   count = 0
        #   last position = first position 
        #   iterate thru the positions
        #       if last position - curr >= mid
        #           increment count
        #           last position = ith ele
        #   if total ball >= m
        #       res = f
        #       increment f = mi + 1
        #   else
        #       decrement f = mid - 1
        # return res
        
        position.sort()
        l = 0
        r = position[-1] - position[0]
        res = 0
        while l <= r:
            mid = (l + r) // 2
            count = 1
            last_position = position[0]

            for p in position:
                if p - last_position >= mid:
                    count += 1
                    last_position = p
            
            if count >= m:
                res = mid
                l = mid + 1

            else:
                r = mid - 1
            
        return res

        # wanna add more balls --> need to reduce force


        