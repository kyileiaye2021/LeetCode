class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        # hashmap = {}

        # for i, n in enumerate(nums):
        #     if n in hashmap:
        #         diff = i - hashmap[n]
        #         if diff <= k:
        #             return True

        #     hashmap[n] = i
        
        # return False

        # sliding window
        # set 
        # iterate thru the ele
        #   if the size of set becomes > k
        #       remove the ith ele 
        #       increment the i by 1
        #   if the curr jth ele in the set
        #       return True
        #   add the curr jth ele to the set
        # return False
        
        i, j = 0, 0
        hashSet = set()

        while j < len(nums):
            if len(hashSet) > k:
                hashSet.remove(nums[i])
                i += 1

            if nums[j] in hashSet:
                return True

            hashSet.add(nums[j])

            j += 1
        
        return False





           