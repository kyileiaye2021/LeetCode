class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # happy cases
        # [1,1,2]
        # [1,2, _]

        # [1,2,3]
        # [1,2,3]

        # [1,2,3,3]
        # [1,2,3,_]

        # [1,1,1,2,2,2,3,3,3]
        # [1,2,3,_,_,_,_,_,_]

        # edge cases
        # [1,1,1,1]
        # [1,_,_,_]

        # [1]
        # [1]

        # []
        # []

        # 2 pointers
        # l,r
        # l = 0
        # r = l + 1
        # until r reaches the end
        # keep moving r until the l and r ele are the same
        # if l and r ele not same
        #   move r pointer ele to l + 1 place
        #   move l to r
        #   move r to l + 1
        # return first k ele of the list

        if len(nums) == 0:
            return []

        l = 0
        r = l + 1
        k = l + 1

        while r < len(nums):
            if nums[r] == nums[l]:
                r += 1
            
            else:
                nums[k] = nums[r]
                k += 1
                l = r
                r = l + 1

        return k


        

        