class Solution:
    def romanToInt(self, s: str) -> int:
        # total = 0
        # roman_num = {}
        # iterate thru the the chars
        #   if curr == 'V' or curr == 'X'
        #       if i > 0 and prev one == 'I' 
        #           total -= 1
        #   if curr == 'L' or curr == 'C'
        #       if i > 0 and prev == 'X'
        #           total -= 10
        #   if curr == 'D' or curr == 'M'
        #       if i > 0 and prev = C
        #           total -= 100
        #   total += roman_num[curr]

        # return total
        total = 0
        roman_num_map = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
        for i in range(len(s)):

            if s[i] == 'V' or s[i] == 'X':
                if i > 0 and s[i - 1] == 'I':
                    total -= 2

            if s[i] == 'L' or s[i] == 'C':
                if i > 0 and s[i - 1] == 'X':
                    total -= 20

            if s[i] == 'D' or s[i] == 'M':
                if i > 0 and s[i - 1] == 'C':
                    total -= 200

            total += roman_num_map[s[i]]

        return total
        

