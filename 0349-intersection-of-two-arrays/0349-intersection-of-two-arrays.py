class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums 1 = [1,2,2,1], nums 2 = [2,2]
        # [2]

        # [4,9,5], [9,4,9,8]
        # [4, 9]

        # set
        # iterate thru nums1
        #   check if the curr ele is in nums2
        #       add it to set
        # change set to list and return the list

        hash_set = set()
        nums2 = set(nums2)

        for n in nums1:
            if n in nums2:
                hash_set.add(n)
        
        return list(hash_set)