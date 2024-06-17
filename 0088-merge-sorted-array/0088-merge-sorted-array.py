class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #create two pointers: last indices of nums1 an nums2
        #iterate over the nums1 from the last ele
        #compare the nums1 and nums2
        #insert the larger ele in the current position
        #if the index of nums1 is less than 0 and the index of nums2 isn't, insert the curr ele of nums2

        '''
        nums1_curr_index = m-1
        nums2_curr_index = n-1
        current_list_index = m + n - 1


        while nums1_curr_index >= 0 and nums2_curr_index >= 0:
            if nums1[nums1_curr_index] < nums2[nums2_curr_index]:
                nums1[current_list_index] = nums2[nums2_curr_index]
                nums2_curr_index -= 1
            else:
                nums1[current_list_index] = nums1[nums1_curr_index]
                nums1_curr_index -= 1
            current_list_index -= 1

        while nums2_curr_index >= 0:
            nums1[current_list_index] = nums2[nums2_curr_index]
            nums2_curr_index -= 1
            current_list_index -= 1
        '''

        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
        
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
