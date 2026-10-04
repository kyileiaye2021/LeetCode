class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sort by end time
        # iterate thru points
        #   check if the curr interval isn't overlapped with prev
        #       res += 1
        #   

        res = 1

        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        for i in range(len(points)):
            start, end = points[i]

            if start <= prev_end:
                prev_end = min(end, prev_end)
            else:
                res += 1
                prev_end = end

        return res
            

