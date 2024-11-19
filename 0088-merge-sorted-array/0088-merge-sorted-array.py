class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # happy cases
        # input: nums1 = [1,2,3,0], nums2 = [1]
        # output: nums1 = [1,1,2,3]

        # edge cases
        # input: nums1 = [0], nums2 = [1]
        # output: nums1 = [1]

        # input: nums1 = [1], nums2 = []
        # output: nums1 = [1]

        # Brute Force
        # two pointer 

        # low level steps
        # m, n - pointers
        # get smaller num from m and n
        # assigned position to the last index in the list
        # iterate until the smaller num becomes 0
        #   check if the m ele of nums1 is greater than or equal to nums2
        #       put the m ele to the assigned pos
        #       decrement assigned pos by 1
        #       decrement m by 1
        #   else:
        #       put the n ele to the assigneed pos
        #       decrement n by 1
        #       decrement assigned pos by 1

        # if m > 0:
        # iterate until assigned pos becomes 0
        #   put the m ele to assigned pos
        #   decrement assigned pos by 1
        #   decrement m by 1

        # if n > 0:
        # iterate until assigned pos becomes 0
        #   put n ele to assigned pos
        #   decrement assigned pos by 1
        #   decrement n by 1

        assigned = m + n - 1

        m = m - 1 
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[assigned] = nums1[m]
                m -= 1
            
            else:
                nums1[assigned] = nums2[n]
                n -= 1

            assigned -= 1

        while m >= 0:
            nums1[assigned] = nums1[m]
            m -= 1
            assigned -= 1

        while n >= 0:
            nums1[assigned] = nums2[n]
            n -= 1
            assigned -= 1






        