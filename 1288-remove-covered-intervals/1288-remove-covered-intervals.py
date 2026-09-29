class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:

        # sort by start
        # prevEnd = first interval endtime
        # count = len(intervals)
        # iterate thru sorted intervals
        #   if start <= prevEnd and end <= prevEnd
        #       count -=1 
        #       prevEnd = max(prevEnd, currEnd)
        #   else:
        #       prev End = curr end
        # return count

        intervals.sort(key=lambda x: (x[0], -x[1]))
        prevEnd = intervals[0][1]
        count = len(intervals)

        for start, end in intervals[1:]:
            if start <= prevEnd and end <= prevEnd:
                count -= 1
                prevEnd = max(prevEnd, end)
            
            else:
                prevEnd = end

        return count