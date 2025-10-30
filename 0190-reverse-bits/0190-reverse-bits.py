class Solution:
    def reverseBits(self, n: int) -> int:

        # move each bit to its corresponding reverse bit position
        # iterate thru the bit
        #   move the bit to the rightmost and extract the curr bit with &
        #   move the curr bit to the corresponding reverse bit position
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        return res

        