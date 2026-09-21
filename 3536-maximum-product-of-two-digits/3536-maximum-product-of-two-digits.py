class Solution:
    def maxProduct(self, n: int) -> int:
        # happy cases
        # n = 10
        # output = 0

        # n = 55
        # output = 25

        # n = 123
        # output = 6

        # n = 515
        # output = 25

        # n = 550
        # output = 25

        # n = 500
        # output = 0

        # break down n to digits and store in arr
        # i , j
        # while j < len(digits):
        #   product = i ele x jele
        #   max_product = max(product, max product)
        #   if i ele > j ele
        #       i = j
        #       j +=1
        #    else: j += 1

        # return max product

        digits = []
        while n != 0:
            digits.append(n % 10)
            n = n // 10

        i = 0
        j = 1
        max_product = float('-inf')
        while j < len(digits):
            product = digits[i] * digits[j]
            max_product = max(max_product, product)
            if digits[i] < digits[j]:
                i = j

            j += 1
        return max_product

