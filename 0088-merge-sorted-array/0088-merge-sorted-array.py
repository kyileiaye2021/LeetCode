class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # since we have to assign ele in nums1 in place
        # there are 0s at the end of nums, we have to sort by large one and assign those
        #
        # i, j = m - 1, n - 1
        # if n = 0, return nums1
        # if m = 0, return nums2
        # k - end index of nums1

        # while i >= 0 and j >= 0
        #   check if i ele > jele
        #       assign i ele to k 
        #       decrement i
        #   else
        #       assign j ele to k
        #       decrement j
        #   decrement k

        i = m - 1
        j = n - 1
        # if n == 0:
        #     return nums1

        # if m == 0:
        #     nums1 = nums2

        k = len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
        