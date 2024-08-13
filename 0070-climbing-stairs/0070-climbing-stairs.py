class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # Happy Case
        # in - n = 2
        # out - 2

        # in - n = 3
        # out - 3

        # in - n = 4
        # * 1,1,1,1
        # * 1,1,2
        # * 1, 2, 1
        # * 2, 1, 1
        # * 2, 2
        # out - 5

        # in - 5
        # * 1,1,1,1,1
        # * 1,2,2
        # * 2, 1, 2
        # * 2,2, 1
        # * 1,1, 1, 2
        # * 1, 2, 1, 1
        # * 1,1,2,1
        # * 2, 1,1, 1
        # out - 8

        '''Edge cases'''
        # in - n = 0
        # out - 1

        # in - n = 1
        # out - 1
        
        '''Dynamic Programming'''
        # check if n is 0 or 1
        #   return 1
        # iterate from 2 to n 
        #   ways to reach curr step is the sum of prev1 steps and prev2 steps
        #   update prev1 val with prev2 val
        #   update prev2 val with curr val
        # return prev2
        
        if n == 0 or n == 1:
            return 1
        
        prev1, prev2 = 1, 1
        
        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
            
        return prev2
        