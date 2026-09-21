class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        hashmap = {}

        for i, n in enumerate(nums):
            if n in hashmap:
                diff = i - hashmap[n]
                if diff <= k:
                    return True

            hashmap[n] = i
        
        return False

           