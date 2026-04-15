class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap + sort + k (O(nlogn))
        # priority queue with (freq count, ele) heap -> O(nlogn) in the worst case scenario
        # bucket sort size - highest freq count
        
        freq_map = Counter(nums) #O(n)
        # hq = []
        
        # for ele, freq in freq_map.items(): #O(mlogn) # m = num of unique ele
        #     heapq.heappush(hq, (-freq, ele))
        
        # res = []
        # for i in range(k): #O(klogn)
        #     freq, ele = heapq.heappop(hq)
        #     res.append(ele)

        # {1:3, 2:2, 3:1}
        size = max(freq_map.values())
        bucket = [[] for _ in range(size + 1)] #[[],[3],[2],[1]]
        
        for ele, freq in freq_map.items():
            bucket[freq].append(ele)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for ele in bucket[i]:
                if k == 0:
                    break
                res.append(ele) # [1, 2]
                k -= 1

        return res