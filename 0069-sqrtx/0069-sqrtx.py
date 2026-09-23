class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 1
        r = x
        res = 0

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if x == square:
                return mid

            elif x > square:
                res = mid
                l = mid + 1

            else:
                r = mid - 1

        return res