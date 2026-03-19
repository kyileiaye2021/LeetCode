class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # recur(i, cur_lst)
        # base case
        # if i >= len(nums)
        #   return

        # for j in range(i, len(nums)):
        #   if j > i and if nums[j] == nums[j - 1]
        #       skip
        #   add the curr ele j to cur lst
        #   add cur list to res
        #   call recur on j+1 ele
        #   pop the cur list

        # recur(0, [])
        # return res

        nums.sort()
        res = [[]]
        cur_lst = []

        def recur(i, cur_lst):
            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                cur_lst.append(nums[j])
                res.append(cur_lst.copy())
                recur(j + 1, cur_lst)
                cur_lst.pop()

        recur(0, cur_lst)
        return res



        