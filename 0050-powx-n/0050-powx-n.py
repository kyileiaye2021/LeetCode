class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x = 2, n = 5
        # x^2 * x^2 * x^1
        
        # n = 5
        # n = n // 2 =2; rem = 1
        # n = n // 2 = 1; rem = 0

        inverse = n < 0
        n = abs(n)
        
        res = 1
        while n:
            rem = n % 2 # 1
            if rem % 2:
                res = res * x # 32
            n = n // 2 # 0
            x = x * x # 256

        return res if not inverse else 1/res
        # def recur_pow(rem, n, x):
            # base case

            # recursive
