class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        
        # sort the trips by end time
        # end time, num of pass in min heap

        # iterate thru trips
        #   total += curr trip people
        #   while min heap and min heap first endtime < curr start
        #       pop out first end time and pass 
        #       total -= pass
        #   add the curr end time and pass in to min heap
        #   if total > cap
        #       return False

        # return true

        trips.sort(key=lambda x: x[1])

        minH = []
        total = 0

        for passengers, start, end in trips:
            total += passengers
            while minH and minH[0][0] <= start:
                prevEnd, prevPass = heapq.heappop(minH)
                total -= prevPass
            if total > capacity:
                return False
            heapq.heappush(minH, (end, passengers))

        return True

            