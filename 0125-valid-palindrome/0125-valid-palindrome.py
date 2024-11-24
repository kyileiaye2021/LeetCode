class Solution:
    def isPalindrome(self, s: str) -> bool:
        # happy case
        # input: s = 'A man, nama'
        # output: True amannama

        # input: s = 'Bar'
        # output: False

        # edge case
        # input: s = ""
        # output: True

        # input: s = "a"
        # output: False

        # i, j
        # while i is less than j
        #   if i ele is a whitespace or special char:
        #       increment i by 1
        #   elif j ele is a whitespace or special char:
        #       decrement j by 1
        #   check if the i char is the same as j char
        #       increment i by 1
        #       decrement j by 1
        #   if they are not same 
        #       return False

        # time - O(logn)
        # space - O(1)

        i, j = 0, len(s)-1
        while i <= j: 
            if not s[i].isalnum(): # if the ele is not alnum
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False

        return True
