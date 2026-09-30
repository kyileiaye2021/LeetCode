class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # while n > 1:
        #   res = n // 2
        #   if res % 2:
        #       return False
        # return True

        # trick: n & (n - 1) remove the lowest bit
        # n           = 101100
        # n - 1       = 101011
        # n & (n - 1) = 101000   → the lowest 1 bit is gone
        # power of 2 only has 1 set bit (removing that makes the final res bits = all 0s)
        
        # if n <= 0:
        #     return False

        # while n % 2 == 0:
        #     n //= 2
        
        # return n == 1

        return n > 0 and (n & (n - 1) == 0)

