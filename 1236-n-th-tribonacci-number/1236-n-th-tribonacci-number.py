class Solution:
    def helper(self, n, arr):
        print("n : ", n)
        # base case
        if n <= 2:
            print('Base case: ', n)
            return arr[n]

        # check if the tribonacci of n is already stored in the arr
        #   retrieve that value and return 

        # else: store the tribonacci of that n 
        # call helper func on (n - 1) (n - 2) (n-3)
        # return tribonacci of that n
        if arr[n] != 0:
            return arr[n]
        
        arr[n] = self.helper(n - 1, arr) + self.helper(n - 2, arr) + self.helper(n - 3, arr)
        return arr[n]

    def tribonacci(self, n: int) -> int:
        # use recursion - 3^n time and O(n) space
        # dp

        if n <= 1:
            return n
    
        arr = [0] * (n + 1)
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1

        return self.helper(n, arr)

    