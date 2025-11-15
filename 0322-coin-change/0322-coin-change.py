class Solution:
    def helper(self, coins, amount, dp):
        # base case
        # if amount = 0
        #   return 0

        # check if the remaining amount the fewest no of coins already computed and stored in the dp
        #   return the fewest no of coins for that remaining amount

        # iterate thru the coins 
        #   find the diff between the amount coin and 
        #   call helper func on the diff + 1
        #   check which one is minimum : the value returned from helper or the curr ele stored at curr amount in dp
        #   store in the curr amount 
        # return the fewest no at that curr amount

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        if dp[amount] != float('inf'):
            return dp[amount]

        for c in coins:
            remaining = amount - c
            fewest_coin = self.helper(coins, remaining, dp)
            if fewest_coin != -1:
                dp[amount] = min(dp[amount], 1 + fewest_coin)
        
        if dp[amount] == float('inf'): # after storing values, if the no. of coins at that amount is still inf, we have to return -1 as we don't store anything in the path when the value becomes -1
            dp[amount] =  -1

        return dp[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp arr of size n + 1 all initialized to 0
        # call helper func on coins, amount, dp
        # return the value returned from helper func

        dp = [float('inf')] * (amount + 1)
        return self.helper(coins, amount, dp)



        