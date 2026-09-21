class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # i, j = 0, 1
        # iterate thru j to the end
        #   ith = i ele - 1, jth = jele - 1
        #   currmultiply = ith x jth
        #   update max multiply
        #   if i ele < j ele
        #       move i to j
        #       j += 1
        #   else
        #       move j += 1

        i = 0
        j = 1
        max_product = 0

        while j < len(nums):
            curr = (nums[i] - 1) * (nums[j] - 1)
            max_product = max(max_product, curr)

            if nums[i] < nums[j]:
                i = j

            j += 1

        return max_product


        