class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # carry = 0
        # res = []

        # iterate thrru the digits from right to l
        #   curr = carry + curr
        #   if curr = last
        #       add curr += 1
        #   res.append(curr % 10)
        #   carry = curr // 10
        # if carry != 0 ==> add carry to res
        # return res[:, -1]

        carry = 0
        res = []

        for i in range(len(digits) -1, -1, -1):
            curr = carry + digits[i]

            if i == len(digits) - 1:
                curr += 1
            
            res.append(curr % 10)
            carry = curr // 10

        if carry != 0 and res[-1] == 0:
            res.append(carry)

        return res[::-1]

        