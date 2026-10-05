class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # 16
        # 16 // 2 == 8; rem = 0
        # 8 // 2 = 4; rem = 0
        # 4 // 2 = 2; rem = 0
        # 2 // 2 = 1; rem = 0
        # 1 // 2 = 0; rem = 1

        # 20
        # 20 // 2 = 10; rem = 0
        # 10 // 2 = 5; rem = 0
        # 5 // 2 = 2; rem = 1 # res = odd num
        # 2 // 2 = 1; rem = 0
        # 1 // 2 = 0; rem = 1

        # 3 
        # 3 // 2 = 1; rem = 1
        # 1 // 2 = 0; rem = 1

        # while n != 1:
        #     rem = n % 2
        #     n = n // 2
        #     if rem % 2:  
        #         return False

        # return True

        if n == 0:
            return False

        def recur_power(n, rem):
            # base case
            if rem % 2:
                return False

            if n == 1: 
                return True

            # recursive case
            return recur_power(n // 2, n % 2)

        return recur_power(n, 0)
