class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # happy case
        # input = ["H", "a", "p"]
        # output = ["p", "a", "H"]

        # edge case
        # input = ["H"]
        # output = ["H"]

        l, r = 0, len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        
        return s