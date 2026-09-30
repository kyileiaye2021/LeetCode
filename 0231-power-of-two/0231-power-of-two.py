class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # while n > 1:
        #   res = n // 2
        #   if res % 2:
        #       return False
        # return True

        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2
        
        return n == 1

