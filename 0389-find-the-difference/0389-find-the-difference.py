class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # happy cases
        # s = 'abcd', t = 'abcde'
        # 'e'

        # s = '', t = 'y
        # y

        # edge cases
        # 'abc', 'acbc'
        # c

        # hashmap
        # itereate thru t
        #   check if curr char in hashmap
        #       decrement the count of curr char
        #       if count = 0, delete the char from the hashmap
        #   else
        #       return the curr char

        s_map = Counter(s)

        for char in t:
            if char in s_map:
                s_map[char] -= 1
                if s_map[char] == 0:
                    del s_map[char]

            else:
                return char


