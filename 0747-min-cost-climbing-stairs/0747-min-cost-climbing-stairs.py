class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        # check if the len of cost is 1 
        #   return the cost[0]
        # add 0 to the arr at the end
        # iterate thru the arr from index 2
        #   val1 = add i - 1 ele to ith ele
        #   val2 = add i - 2 ele to ith ele
        #   get min of val1 and val2 
        #   assign the min to the ith pos
        # return the last ele of the arr

        cost.append(0)
        for i in range(2, len(cost)):
            val1 = cost[i] + cost[i - 1]
            val2 = cost[i] + cost[i - 2]
            cost[i] = min(val1, val2)

        return cost[-1]



        