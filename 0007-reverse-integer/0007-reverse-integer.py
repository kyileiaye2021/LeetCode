class Solution:
    def reverse(self, x: int) -> int:
        # if x < 0:
        #   x = -1 * x
        # while x != 0
        #   divide x / 10
        #   x = x % 10
        #   add remainder to the res list
        # iterate thru the res list
        #   if i == 0
        #       while curr ele == 0: go to next index
        # res = int(''.join(res[i:]))
        # if orig x < 0:
        #   return -res else res

        max_val = 2**31 - 1
        min_val = -2**31
        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > max_val // 10 or (res == max_val // 10 and digit > max_val % 10):
                return 0

            if res < min_val // 10 or (res == min_val // 10 and digit < min_val % 10):
                return 0

            res = (res * 10) + digit 

        return res

