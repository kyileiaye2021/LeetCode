class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        memo = {}

        def recur(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            best = float('inf')
            for c in coins:
                best = min(best, 1 + recur(rem - c))
                
            memo[rem] = best
            return memo[rem]

        res = recur(amount) 
        
        return res if res != float('inf') else -1

       
