class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
    
        intervals.sort() # sort the list of tuples by first elements in tuples
        print(f"sorted: {intervals}")
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            
            top_tuple = res[-1]
            if intervals[i][0] >= top_tuple[0] and intervals[i][0] <= top_tuple[1]: # if overlapped
                
                # for second ele in the tuple
                if intervals[i][1] >= top_tuple[1]:
                    res.pop()
                    res.append((top_tuple[0], intervals[i][1]))
                    
                # else:
                #     res.add((top_tuple[0], top_tuple[1]))
                    
            else: # if not overlapped
                res.append(intervals[i])
        
        res = list(res)
        return res