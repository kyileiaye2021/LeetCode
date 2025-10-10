class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # curr_max = first val.in the list
        # maxScore
        # iterate thru the list from the sec ele
        #   decrement the curr_max
        #   find the adjacent ele - 1
        #   update the curr_max with max of curr max and adj ele
        #   maxScore = maxScore , (curr val + curr max)

        curr_max = values[0]
        maxScore = 0

        for i in range(1, len(values)):
            curr_max -= 1
            adj_max = values[i - 1] - 1
            curr_max = max(curr_max, adj_max)
            maxScore = max(maxScore, (curr_max + values[i]))

        return maxScore