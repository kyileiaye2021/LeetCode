class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set
        # regular list iteration

        # res list
        # set
        # create an empty set and populate the set with nums1 ele
        # iterate over the ele in nums2
        #   check if the ele in set and not in the res list yet
        #       append the curr ele
        # return res list

        res = []
        n = []

        for ele in nums1:
            if ele not in n:
                n.append(ele)
        
        for ele in nums2:
            if ele in n and ele not in res:
                res.append(ele)

        return res

