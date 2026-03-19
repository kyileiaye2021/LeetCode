class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_lst = []

        def recur(cur_lst):
            if len(cur_lst) == len(nums):
                res.append(cur_lst.copy())
                return

            for j in range(len(nums)):
                if nums[j] in cur_lst:
                    continue
                
                cur_lst.append(nums[j])
                recur(cur_lst)
                cur_lst.pop()

        recur(cur_lst)
        return res



        