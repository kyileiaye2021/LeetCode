class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        max_alt = 0

        for i in range(len(gain)):
            prefix = prefix + gain[i]
            max_alt = max(max_alt, prefix)

        return max_alt


        