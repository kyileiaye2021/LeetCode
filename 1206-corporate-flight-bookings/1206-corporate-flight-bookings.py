class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        # create an arr of size n all vals initialized to 0
        # iterate thru the bookings
        #   iterate thru from first to last (i)
        #       add the curr val to i - 1 th position in the res arr
        # return res

        # brute force O(n * num of booking)
        # res = [0] * n

        # for first, last, val in bookings:
        #     for i in range(first - 1, last):
        #         res[i] += val

        # return res

        # create interval arr
        # iterate thru the list
        #   keep track of first 
        #   keep track of last
        # 
        # create res arr
        # iterate thru res arr
        #   add diff[i] to curr
        #   assign curr to curr[i]
        # return res

        interval = [0] * (n + 1)

        for first, last, val in bookings:
            interval[first - 1] += val
            interval[last] -= val

        res = [0] * n
        curr = 0
        for i in range(len(interval) - 1):
            curr += interval[i]
            res[i] = curr

        return res
         
            

        

