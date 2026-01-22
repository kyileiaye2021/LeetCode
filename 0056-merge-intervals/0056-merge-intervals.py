class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # list to store the curr time intervals
        # add the first interval into the curr time
        # iterate the intervals from second ele
        #   start <= last start
        #   start <= last end
        #   update the last interval with the min of start and min of end
        # add the curr interval to curr time
        # update the start and last
        intervals.sort()
        res = [intervals[0]]
        s = intervals[0][0]
        e = intervals[0][1]
        for start, end in intervals:
            # merge
            if start <= e:
                s = min(start, s)
                e = max(end, e)

                res[-1] = [s, e]

            else:
                res.append([start, end])
                s = start
                e = end

        return res


        