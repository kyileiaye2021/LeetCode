class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # happy cases
        # [4,5,2]
        # [4,5,2,4,5,2]

        # edge cases
        # [9]
        # [9,9]

        # []
        # []
        return nums + nums
        