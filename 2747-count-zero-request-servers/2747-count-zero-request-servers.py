class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        # creat hashmap {time: set(servers)}
        # res = []
        # freq map
        # sort the logs by time
        # sort the queries
        # l = 0
        # r = 0
        # iterate thru the queries
        #   [i, j] = create a range for query
        #   while r ele <= j:
        #       add freq_map[log[r][0]] with increment count of 1
        #   while l ele < i:
        #       decrement freq_map[log[l][0]] 
        #       if count == 0: del that ele from freq map
        #   inactive_server = n - len(freq_map)
        #   res.append(inactive_server)
        #   return res

        res = [0] * len(queries)
        freq = {}
        logs.sort(key=lambda x: x[1])

        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()

        l = 0
        r = 0

        for q, i in queries:

            s, e = q - x, q
            
            # expanding 
            while r < len(logs) and logs[r][1] <= e:
                freq[logs[r][0]] = freq.get(logs[r][0], 0) + 1
                r += 1

            # shrinking
            while l < len(logs) and logs[l][1] < s:
                freq[logs[l][0]] = freq.get(logs[l][0], 0) - 1
                if freq[logs[l][0]] == 0:
                    del freq[logs[l][0]]
                l += 1

            inactive = n - len(freq)
            res[i] = inactive

        return res

            






