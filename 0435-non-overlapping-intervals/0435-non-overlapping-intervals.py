class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # we want max num of intervals left
        # sort intervals by end time

        intervals.sort(key=lambda x: x[1])

        last_end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                last_end = min(end, last_end)
                count += 1
            else:
                last_end = end
        return count

