class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # hashmap
        # {ele: index}
        # iterate thru the ele
        #   if ele not in hashmap
        #       add with the curr index
        #   else
        #       check if the diff between curr index and prev index <= k
        #           return true
        #       else:
        #           assign the curr index to the prev index
        # return false

        map = {}
        for i in range(len(nums)):
            
            if nums[i] in map:
                diff = i - map[nums[i]]
                if diff <= k:
                    return True

            map[nums[i]] = i

        return False
        