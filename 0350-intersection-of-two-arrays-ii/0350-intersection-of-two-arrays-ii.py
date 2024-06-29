class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Can there be no intersection numbers in two arrays? #no
        # Can either of the arrays be empty or null? #no
        
        # High Level Planning
        # * Brute Force Approach
        #   * Iterate over the list nums1 and check if the curr ele in nums2. If
        #     it is, put it in the new list
        # * Two pointer approach
        #   * move unique ele to the end of the array and delete those unique ele
        #   * remove the checked ele in the array to avoid double counting
        
        # Low Level Planning
        # * Two Pointer Approach
        # * create a list to store the intersection elements
        # * create a pointer to store the common number index
        # * create a dict to store nums2 ele and its occurence
        # * iterate over the list nums1
        #   * check if the curr ele is in nums2_dict key and its value is > 0
        #       * put the ele in the position that the common number index currently 
        #         points to
        #       * increment common number index by 1
        #       * decrement the occurence of that num in nums2 dict
        # * delete the list from the common number index to the end
        # * return the list
        
        #intersection_lst = []
        common_num_index = 0
        nums2_dict = {}
        for ele in nums2:
            if ele not in nums2_dict:
                nums2_dict[ele] = 1
            else:
                nums2_dict[ele] += 1
                
        for ele in nums1:
            if ele in nums2_dict and nums2_dict[ele] > 0:
                nums1[common_num_index] = ele
                common_num_index +=1
                nums2_dict[ele] -= 1
        del nums1[common_num_index:]
        return nums1
        