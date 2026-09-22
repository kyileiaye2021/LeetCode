class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # iterate thru the rows
        #   total = 0
        #   iterate thru the cols
        #       total += curr row curr col
        #   update max wealth 
        # return max wealth

        max_wealth = 0

        m = len(accounts)
        n = len(accounts[0])

        for i in range(m):
            total = 0
            for j in range(n):
                total += accounts[i][j]
            max_wealth = max(max_wealth, total)

        return max_wealth
                
