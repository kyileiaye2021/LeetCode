class Solution:
    def myAtoi(self, s: str) -> int:

        # "  gta123"
        # 0

        # "12-45"
        # 12

        # "0056et"
        # 56

        # "-30u"
        # -30

        # "000"
        # 0
        # iterate thru str
        # if curr char is an alphabet
        #   break
        # if cur char is " " -> continue
        # if cur char is at index 0 and '-' 
        #   add it to res
        # if cur char is digit
        #   if it is 0 
        #       if len(res) == 0 or res[-1] == '-'
        #           continue
        #   add cur char to res
        # return int(res)

        # strip whitespaces
        s = s.strip(" ")

        if not s:
            return 0

        sign = 1
        res = ""
        index = 0

        # for signs
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        while index < len(s):
            if s[index].isdigit():
                res += s[index]
                index += 1
            else:
                break
        if not res:
            return 0
        res = int(res) * sign

        # 6. Clamp the result:
        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1

        return res
        




        