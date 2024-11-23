class Solution:
    
    def isHappy(self, n: int) -> bool:

        # happy cases
        # input: n = 10
        # output: true

        # input: n = 12
        # output: false

        # edge cases
        # input: n = 1
        # output: true

        # input: n = 5
        # output: false

        # plan
        # check if the number is 1
        #   return true
        # check if the number is less than 10
        #   return false
        # sum = 0 
        # iterate until num becomes 1
        #   iterate until num % 10 becomes 0
        #       digit = num % 10
        #       square = digit **2
        #       accumulate the sum with the digits
        #   if sum is 1
        #       return true
        #   else if sum is less than 10: return false
        #   else: update num with sum

        visited = []

        if n == 1:
            return True

        sum = 0
        while n != 1:
            if n not in visited:
                visited.append(n)
            else:
                return False
            while n != 0:
                digit = n % 10
                n = n // 10
                sum += (digit**2)

            if sum == 1:
                return True

            else:
                n = sum
                sum = 0


    

        