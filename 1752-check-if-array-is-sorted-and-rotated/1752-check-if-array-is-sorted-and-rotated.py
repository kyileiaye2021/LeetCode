class Solution:
    def check(self, nums: list[int]) -> bool:

        # the first is < last
        # just check if all elements are sorted

        # else
        # find the position where the rotated pos begin

        # starting from that position, find if the elements are sorted
        N = len(nums)
        count = 1

        if N == 1:
            return True
        
        for i in range(1, 2 * N):
            if nums[i % N] >= nums[(i - 1) % N]:
                count += 1
            
            else:
                count = 1

            if count == N:
                return True
        
        return False
            
            


    