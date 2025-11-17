class Solution:
    def dp_helper(self, i, amount, coins, memo):
        # base case
        if i >= len(coins) or amount < 0:
            return 0
        
        if amount == 0:
            return 1

        # retrieve from cache if the count is already stored
        if (i, amount) in memo:
            return memo[(i, amount)]

        # include the curr ith ele
        include = self.dp_helper(i, amount - coins[i], coins, memo)

        # exclude the curr ith ele
        exclude = self.dp_helper(i + 1, amount, coins,memo)

        # num of counts from 2 paths
        memo[(i, amount)] = include + exclude
        return memo[(i, amount)]

    def change(self, amount: int, coins: List[int]) -> int:
        memo:Dict[Tuple(int, int),int] = {}
        return self.dp_helper(0, amount, coins, memo)
        
        # recursion
        # base case
        # if the amount == 0
        #   increment the count by 1
        #   return 
        # if amount < 0
        #   return 0

        # iterate thru the coins
        #   diff = amount - curr coin
        #   return call recursive on the diff
        
        