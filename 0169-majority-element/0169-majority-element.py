class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1

        for n, freq in map.items():
            if freq > (len(nums) // 2):
                return n

       # hashmap to count freq of nums
       # iterate thru the hashmap
       #    check if the curr val is > n // 2
       #        return that key

    
