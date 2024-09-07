class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Happy cases
        # input: nums1 = [1,2,2,1], nums2 = [2,2]
        # output: [2,2]
        
        # Edge cases
        # input: nums1= [1,2,4], nums2 = [3,5]
        # output: []
        # input: nums1 = [2], nums2 = [4]
        # output: []
        
        # Hashmap Approach
        # create a list res_lst to store the intersection ele
        # create a hashmap freq_map for nums1
        # iterate over nums1
        #   check if the curr ele is in freq_map
        #       increment the value of curr ele by 1
        #   else: set it in the map with value 1
        # iterate over the nums2
        #   check if the curr ele is in freq_map
        #       check if the value of the curr ele in hashmap is greater than 0
        #           decrement it by 1
        #           append the ele in the res_lst
        # return the res_lst
        
        # Time complexity - O(m + n)
        # Space complexity - O(m + n)
        res_lst = []
        freq_map = {}
        for ele in nums1:
            if ele not in freq_map:
                freq_map[ele] = 1
            else:
                freq_map[ele] += 1
                
        for ele in nums2:
            if ele in freq_map:
                if freq_map[ele] > 0:
                    freq_map[ele] -= 1
                    res_lst.append(ele)
        
        return res_lst