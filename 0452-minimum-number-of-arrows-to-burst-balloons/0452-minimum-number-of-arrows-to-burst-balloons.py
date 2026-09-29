class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        # sort points by start
        # prevEnd = first interval end time
        # numShot = 0
        # iterate thru sorted points
        #   check if curr interval is overlapped with prev interval
        #       get min val between prevEnd and curr interval endtime and set prevend
        #   else
        #       set prevend to curr interval endtime
        #       numShot +=1
        # return numShot

        # Note: a new arrow is used only when the curr interval doesn't overlap

        points.sort(key=lambda x: x[0])
        prevEnd = points[0][1]
        numShot = 1

        for start, end in points[1:]:
            if start <= prevEnd:
                prevEnd = min(prevEnd, end)

            else:
                numShot += 1
                prevEnd = end

        return numShot
