class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq map
        # iterate thru the ele and check if their freq is > threshold
        # O(n) space and O(n) time

        freq = {}
        res = []
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for n, count in freq.items():
            if count > (len(nums) // 3):
                res.append(n)

        return res