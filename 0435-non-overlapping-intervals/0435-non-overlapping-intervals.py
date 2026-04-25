class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if s < last_end: # overlapping
                count += 1
                last_end = min(e, last_end)

            else:
                last_end = e
        
        return count
            


            