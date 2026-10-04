class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # res
        # res.append(intervals[0])
        # iterate thu the intervals
        #   check if the newInterval start < curr end
        #   new interval start and end
        #   add it to res
        #   else
        #       add it to res

        res = []
        new_start = newInterval[0]
        new_end = newInterval[1]

        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < new_start: # curr interval before new start
                res.append([start, end])

            elif start > new_end:
                res.append([new_start, new_end])
                return res + intervals[i :]

            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        res.append([new_start, new_end])
        return res

