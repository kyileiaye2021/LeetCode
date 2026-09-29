class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n < 0: 
        #     x = 1 / x
        #     n = -1 * n
        # res = 1
        # for i in range(1, n + 1):
        #     res = res * x

        # return res

        def helper(x, n):

            # base case
            if x == 0:
                return 0

            if n == 0:
                return 1

            # recursive case
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n)) 
        return res if n >= 0 else 1 / res

