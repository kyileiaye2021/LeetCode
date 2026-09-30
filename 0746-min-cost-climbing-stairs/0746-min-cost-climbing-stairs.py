class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        # recur_func(i, total)
        # base case
        #   if i >= len(cost)
        #       return 0
        # recursive case
        #   total += cost[i]
        #   keep track of min total
        #   recur_func(i + 1, total)
        #   total -= cost[i]
        #   keep track of min total
        #   recur_fun(i + 2, total)

        arr = [-1] * (len(cost))

        def recur(i):
            # base case
            if i >= len(cost):
                return 0

            # recursive case
            if arr[i] != -1:
                return arr[i]
            arr[i] = cost[i] + min(recur(i + 1), recur(i + 2))
            return arr[i]

        return min(recur(0), recur(1)) 