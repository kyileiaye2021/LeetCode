class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # happy cases
        # input: nums1 - [1, 2, 3], num2 - [3,4,5]
        # output - [3]

        # edge cases
        # input: nums1 - [1,2,2], nums2 - [2,3]
        # output - [2,2]

        # input: nums1 - [1], nums2 - [2]
        # output - []

        # hashmap 
        # time - O(n + m)
        # space - O(2n)
        freq = {}
        res = []
        for ele in nums2:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        for ele in nums1:
            if ele in freq and freq[ele] > 0:
                freq[ele] -= 1
                res.append(ele)

        return res