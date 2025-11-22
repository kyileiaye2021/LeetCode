class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        # if the total sum is even
        #   we can only get odd curr num onlly if we remove odd prefix from even curr sum

        # if the total sum is odd
        #   we can only get odd curr num only if we remove even prefix right?

        curr_sum = 0
        even_count = 0
        odd_count = 0
        res = 0
        MOD = (10 ** 9) + 7

        for n in arr:

            curr_sum += n

            if curr_sum % 2: # odd
                res = (1 + res + even_count) % MOD
                odd_count += 1
                
            else:
                res = (res + odd_count) % MOD
                even_count += 1

        return res