class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # brute force
        # add new interval
        # last end = first end time
        # res list # O(n) time 
        # iterate thru the intervals
        #   check if last end >= cur s time
        #       update last item in res list
        #       prev_s, prev_e = res_lst[-1]
        #       res_lst[-1][1] = e
        #       last end = e
        #   else:add the curr interval to res lst
        # return res

        # store new interval in the max heap
        # iterate thru the intervals
        #   if curr end > new interval s:
        #       if curr s < new interval e:
        #           new interval s = min(cur_s, s)
        #           new interval e = max(cur_e, e)
        #       else
        #           add (s, e) in the res
        #   else: add (s, e) in the res
        # return res

        res = []
        for i, [cur_s, cur_e] in enumerate(intervals):
            if cur_e >= newInterval[0]:
                if cur_s <= newInterval[1]:  # overlapped
                    newInterval[0] = min(cur_s, newInterval[0])
                    newInterval[1] = max(cur_e, newInterval[1])

                else: # new interval is added and everything after that is added
                    res.append([newInterval[0], newInterval[1]])
                    return res + intervals[i:]

            else: # new interval is added 
                res.append([cur_s, cur_e])
        
        res.append([newInterval[0], newInterval[1]])
        return res


        