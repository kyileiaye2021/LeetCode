class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # iterate thru the list
        #   separate the str into 2 nums
        #   calculate the min and hr and convert to minute
        #   reassign the minute into curr position

        # create a minute list of size 1439 all ele initialized to 0

        # iterate thru the list
        #   assign them to the minute list based on their curr minute

        # min diff set to largest value
        # l and r
        # iterate thru the minute list until r reachees the end
        #   whiile l point doesn't point to 1
        #       move l and r pointers
        #   move r pointer
        #   if r pointer reaches 1
        #       find the window size and update the diff
        # return min diff

        for i in range(len(timePoints)):
            curr_str = timePoints[i]
            if timePoints[i] == '00:00':
                curr_str = "24:00"
            hr, minute = curr_str.split(':')
            hr = int(hr)
            minute = int(minute)
            curr_min = (hr * 60) + minute

            timePoints[i] = curr_min

        print(timePoints)
        minute_list = [0] * 1440

        for time in timePoints:
            minute_list[time - 1] += 1

        min_diff = float('inf')
        l = 0
        r = 1
        temp_start = 0 # first minute
        temp_last = 0 # last minute

        while r < len(minute_list):
            while l < len(minute_list) and minute_list[l] == 0:
                l += 1
                r += 1
                temp_start += 1

            if minute_list[l] >=2 or minute_list[r] >= 2:
                return 0

            elif minute_list[r] == 1:
                curr_diff = r - l 
                min_diff = min(min_diff, curr_diff)
                l = r
                temp_last = r
                r += 1

            elif minute_list[r] == 0:
                r += 1

        print(temp_start)
        print(temp_last)
        edge_minute = 1440 - (temp_last + 1) + (temp_start + 1)
        min_diff = min(edge_minute, min_diff)
        return min_diff