class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        freq = [[] for i in range(len(nums) + 1)] #bucket list
        
        # filling up the frequency map
        for ele in nums:
            if ele not in frequency_map:
                frequency_map[ele] = 1
            else:
                frequency_map[ele] += 1
        
        #filling up the bucket list
        for ele, count in frequency_map.items():
            freq[count].append(ele)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        return res
        
        
        