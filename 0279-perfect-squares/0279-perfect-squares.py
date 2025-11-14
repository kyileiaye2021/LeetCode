class Solution:
    def helper(self, n, arr):
        # base case
        # we have to stop when n becomes 0
        # we have to return the ele if we already store it in the arr
        if n == 0:
            return 0

        if arr[n] != float('inf'):
            return arr[n]

        # try subtracting every perfect square <=n from n
        # and call recursive func on remaining 
        for i in range(1, len(arr)):
            if (i * i) <= n:
                diff = n - (i * i)
                arr[n] = min(arr[n], 1 + self.helper(diff, arr))
            
        return arr[n]

    def numSquares(self, n: int) -> int:
        arr = [float('inf')] * (n  + 1)
        arr[0] = 0
        return self.helper(n, arr)
        # happy cases
        # n = 2
        # output: 2 (1 + 1)

        # n = 3
        # output: 3 (1 + 1 + 1)

        # n = 5
        # output: 2 (1 + 4)

        # n = 6
        # output: 3 (1 + 1 + 4)

        # n = 7
        # output: 4 (1 + 1 + 1 + 4)


        # edge cases
        # n = 4
        # output: 1 

        # edge cases
        # n = 1
        # output: 1

        # recursion
        #   12
        #  / | \
        # 11 8  3
        # continue and get the shortest path





        # store some values and check them before calling recursion?


