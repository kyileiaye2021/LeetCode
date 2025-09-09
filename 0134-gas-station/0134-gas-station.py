class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # detect the circle

        # define the start point first
        # for start point
        # go thru the 2 arrs at the same time
        # compare if gas[i] > cost[i]
        #   set that i pos as the start point
        # if start point is still none --> return -1

        # curr tank = 0
        # curr = start point
        # until curr get back to the start point
        #   add curr gas to curr tank
        #   energy = curr tank - curr cost
        #   if that becomes neg
        #       return -1
        # if curr < len(gas)
        #   increment curr by 1
        # else: reset it to 0

        # i = 0
        # start = None
        # while i < len(gas):
        #     if gas[i] > cost[i]:
        #         start = i
        #         break
        #     i += 1
        
        # if not start:
        #     return -1

        # print(f"Start index: {start}")
        # curr_tank = gas[start]
        # curr = start + 1

        # if curr >= len(gas):
        #     curr = 0

        # while curr != start:
        #     if curr >= len(gas):
        #         curr = 0

        #     print(f"curr: {curr}")
        #     energy = curr_tank - cost[curr - 1]
        #     if energy < 0:
        #         return -1

        #     energy += gas[curr]
        #     print(f"Energy in each step: {energy}")
        #     curr += 1
        # return curr

        # first we need to find if the gas can cover the cost 
        # check if the sum of all gas is >= the sum of all cost
        # 
        # start point
        # get the energy
        # tank += energy 
        # if energy is neg --> go to next ele

        # check if we can go thru the whole loop to get back to the start point
        if sum(gas) < sum(cost):
            return -1

        # for finding start point
        tank = 0
        start = 0
        for i in range(len(gas)):
            energy = gas[i] - cost[i]
            tank += energy

            if tank < 0:
                tank = 0
                start = i + 1

        return start