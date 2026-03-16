class Solution:
    def hammingWeight(self, n: int) -> int:

        # divide the n by 2
        # count = 0
        # until n becomes 0
        #   rem = n % 2
        #   if rem == 1:
        #       count += 1
        #   n = n // 2
        # return c0unt

        count = 0
        while n != 0:
            rem = n % 2
            if rem == 1:
                count += 1
            n = n // 2
        return count    
        