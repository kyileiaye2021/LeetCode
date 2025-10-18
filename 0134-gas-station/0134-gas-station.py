class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # find the total of the gas amount and cost
        # check if it cannnot cover the cost of whole journey
        #   return -1

        # itereate thru the ele in the gas
        #   check if the gas is greater than equal to the cost
        #       return the pos

        res = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res




