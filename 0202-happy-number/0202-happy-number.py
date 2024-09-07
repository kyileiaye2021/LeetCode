class Solution:
    def isHappy(self, n: int) -> bool:
        
        # Happy case
        # n = 19
        # output - True
        
        # Edge case
        # n = 0
        # output - False
        # n - 2
        # output - False
        # n - 1
        # output - True
        
        # if the number is already in the visited hashset, return False
        
        # create a hashset to store the sum of each time
        # check until the n is already in the hashset
        #   get the sum of the square of the digits of n 
        #   check if it is 1
        #       return True
        # return False
        
        # Sumofsquare
        # sum = 0
        # iterate until n becomes 0
        #   n % 10 
        #   sum += n
        #   n = n // 10
        
        visited = set() # memory O(n)
        
        while n not in visited:
            visited.add(n)
            
            n = self.sumOfSquare(n)
            if n == 1:
                return True
            
        return False
        
    def sumOfSquare(self, n):
        sum = 0
        
        while n:
            digit = n % 10
            sum += (digit ** 2)
            n = n // 10
            
        return sum
            
            
        
        
        
     