class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        #Assumption
        # Num is not null
        
        # * Iterative Appraoch
        # * create a set to check the n is already visited or not
        # * iterate until the n is not found in the set
        #   * add n to the set
        #.  * iterate until n is 0
        #       * find n % 10 to get digit
        #       * square that digit and add it to the sum
        #       * update orig n with curr sum
        #   * if n is equal to 1, return True
        #   * return False 
        
        visited_set = set()
        while n not in visited_set:
            visited_set.add(n)
            
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
        