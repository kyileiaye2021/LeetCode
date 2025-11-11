class Solution:
    def climbStairs(self, n: int) -> int:

        # tabulation approoach

        # two pointers to store the num of ways at step 1 and 2, ptr1 = 1 and ptr2 = 2
        # iterate thru from 3 to n
        #   add the two pointers and store in the curr
        #   update ptr1 to ptr2 and ptr2 to curr

        # return curr

        ptr1 = 1
        ptr2 = 2
        if n == 1: 
            return ptr1

        if n == 2:
            return ptr2
            
        curr = 0

        for i in range(3, n + 1):
            curr = ptr1 + ptr2
            ptr1 = ptr2
            ptr2 = curr

        return curr



        # base case
        # if n is 1 or 2 return n
        # call recursive func on the n - 1 and n -2

        # def recur(n):
        #     if n == 1 or n == 2:
        #         return n

        #     return recur(n - 1) + recur(n - 2)
        
        # return recur(n)

        # memoization
        # def recur(n, memo):
        #     # base case
        #     if n == 1 or n == 2:
        #         return n

        #     if memo[n] != -1:
        #         return memo[n]

        #     memo[n] = recur(n - 1, memo) + recur(n - 2, memo)
        #     return memo[n]

        # memo = [-1] * (n + 1)
        # return recur(n, memo)

        
        