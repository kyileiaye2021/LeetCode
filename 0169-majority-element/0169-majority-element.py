class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums = [3,2,3]
        # output: 3

        # nums = [2, 2, 1, 1, 2, 3]
        # output: 2

        # nums = [1,1,1]
        # output: 1

        # nums = [3,2, 2, 3, 2, 3]
        # nums = [1]
        # output: 1

        # # hashmap 
        # freq_map = defaultdict(int)
        # for n in nums:
        #     freq_map[n] += 1
        
        # majority = len(nums) // 2
        # for n, freq in freq_map.items():
        #     if freq > majority:
        #         return n

        # moore voting algorithm
        count = 0
        candidate = 0

        for n in nums:
            if count == 0:
                candidate = n

            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate