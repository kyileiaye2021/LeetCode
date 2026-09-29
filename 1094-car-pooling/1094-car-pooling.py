class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # interval

        # sort the trips by start time
        # max end time = end time of the first trip
        # longest travelling people = passenger in first trip
        # iterate thru the trips from second trip
        #   if start time < max end time
        #       add the num of people from curr trip and longest travelling people
        #       if total > cap
        #           return False
        #   if curr end time > max end time (we can't compare just one prev end time)
        #       max end time = curr end time
        #       longest travelling people = passengers in curr trip
        # return True

        # min heap [[end time, num of pass]]
        # sort the trips by start time
        # iterate thru the sorted trips
        #   while min heap
        #       if curr start time >= end time of first ele in max heap
        #           end time, dropped off passenger = pop the max heap
        #           total -= dropped off passenger
        #       
        #   total += curr passenger
        #   add [curr end time, curr pass] to max heap
        #   if total > cap:
        #      return false
        # return True

        min_heap =[]
        total = 0
        sorted_trips = sorted(trips, key=lambda x: x[1])
        print(sorted_trips)

        for passenger, start, end in sorted_trips:
            while min_heap:
                if start >= min_heap[0][0]:
                    drop_off_time, drop_off_pass = heapq.heappop(min_heap)
                    total -= drop_off_pass
                else:
                    break

            total += passenger
            heapq.heappush(min_heap, [end, passenger])
            if total > capacity:
                return False

        return True

