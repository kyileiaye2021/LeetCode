class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap

        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        #. bucket sort
        bucket = [[] for _ in range(len(nums) + 1)]

        for ele in freq_map:
            bucket[freq_map[ele]].append(ele)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for ele in bucket[i]:
                res.append(ele)
                k -= 1

            if k == 0:
                return res
